from fastapi import APIRouter, status
from schema import train_sm
from yolov5 import train

router = APIRouter(
    prefix="/model_train",
    tags=["train"],
    responses={404: {"description": "Not found"}},
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def train_model(input_data: train_sm.TrainData):
    train.run(data=input_data.yaml_file_path, weights=input_data.yolo_weight_file, epochs = input_data.epochs)
    return {"message": "Training is Compeleted and model is saved into 'output' directory"}

