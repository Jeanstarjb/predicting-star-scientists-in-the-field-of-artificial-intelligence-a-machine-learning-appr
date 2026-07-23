from fastapi import APIRouter, HTTPException, Request
from typing import List
import pandas as pd
from .. import schemas

router = APIRouter(
    prefix="/predict",
    tags=["predictions"]
)

@router.post("/", response_model=schemas.PredictionResult)
async def predict(prediction_input: schemas.PredictionInput, request: Request):
    try:
        model = request.app.state.model
        preprocessor = request.app.state.preprocessor
        
        input_data = pd.DataFrame([prediction_input.dict()])
        processed_data = preprocessor.transform(input_data)
        probability = model.predict_proba(processed_data)[0][1]
        
        return {
            "probability": probability,
            "features": prediction_input.dict(),
            "timestamp": pd.Timestamp.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/feature-importance", response_model=List[schemas.FeatureImportance])
async def get_feature_importance(request: Request):
    try:
        model = request.app.state.model
        if not hasattr(model, 'feature_importances_'):
            raise HTTPException(status_code=400, detail="Model does not support feature importance")
        
        feature_names = model.feature_names_in_
        importances = model.feature_importances_.tolist()
        
        return [{"feature": name, "importance": imp} for name, imp in zip(feature_names, importances)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))