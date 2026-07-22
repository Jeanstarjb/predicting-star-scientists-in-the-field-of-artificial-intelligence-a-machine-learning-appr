from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib
from sqlalchemy.orm import Session
import datetime
from . import models, schemas, preprocessing
from .database import get_db
from .routers import researchers, publications

app = FastAPI()

# Load ML model and preprocessor
try:
    model = joblib.load('model.joblib')
    preprocessor = preprocessing.DataPreprocessor()
except Exception as e:
    raise RuntimeError(f"Error loading model or preprocessor: {e}")

app.include_router(researchers.router)
app.include_router(publications.router)

class PredictionRequest(BaseModel):
    researcher_id: int

@app.post('/predict', response_model=schemas.Prediction)
async def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    researcher = db.query(models.Researcher).filter(models.Researcher.id == request.researcher_id).first()
    if not researcher:
        raise HTTPException(status_code=404, detail="Researcher not found")
    
    publications = db.query(models.Publication).filter(models.Publication.researcher_id == request.researcher_id).all()
    
    current_year = datetime.datetime.now().year
    early_publications = [p for p in publications if (p.publication_date.year - researcher.start_year) <= 5]
    
    features = {
        'start_year': researcher.start_year,
        'h_index': researcher.h_index,
        'early_publications_count': len(early_publications),
        'early_discipline_diversity': len(set(p.journal for p in early_publications)),
        'early_citation_sum': sum(p.citation_count for p in early_publications)
    }
    
    feature_df = pd.DataFrame([features])
    
    try:
        processed_features = preprocessor.transform(feature_df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Feature preprocessing failed: {e}")
    
    try:
        prediction_proba = model.predict_proba(processed_features)
        prediction_score = prediction_proba[0][1]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
    
    db_prediction = models.Prediction(
        researcher_id=request.researcher_id,
        prediction_score=prediction_score
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    
    return {
        'prediction': prediction_score,
        'confidence': prediction_score,
        'prediction_id': db_prediction.id
    }

@app.get('/')
async def health_check():
    return {'status': 'ok'}