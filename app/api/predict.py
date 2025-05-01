from fastapi import APIRouter

from app.schemas.prediction import PredictRequest, PredictResponse
from app.services.model_service import predict_category

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    category = predict_category(request.text)
    return PredictResponse(category=str(category))
