from fastapi import APIRouter, HTTPException, Request
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
        
        return {"starPotential": probability}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")