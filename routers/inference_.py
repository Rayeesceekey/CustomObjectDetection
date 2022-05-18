from fastapi import APIRouter, Response
from schema import inference_sm
from yolov5 import detect
from get_logger import _in_logger
import cv2

router = APIRouter(
    prefix="/model_inference",
    tags=["inference"],
    responses={404: {"description": "Not found"}},
)

@router.post("/from_path")
async def get_prediction_output(input_data: inference_sm.InputDataPath):
    _ = detect.run(source = input_data.image_path, data=input_data.yaml_file_path, weights=input_data.model_path)
    _in_logger.info("Inference Compeleted")
    return {"message": "Inference Compeleted and output images are saved into 'output' directory"}
    

@router.post("/from_image")
async def get_prediction_output(input_data: inference_sm.InputDataImg):
    pre_train_flag=input_data.use_pretrained
    if pre_train_flag == True:
        output_image = detect.run(source = input_data.image_path, data=input_data.yaml_file_path, weights="artifacts/weights/yolov5s.pt")
    else:
        output_image = detect.run(source = input_data.image_path, data=input_data.yaml_file_path, weights=input_data.model_path)
    _, encoded_image = cv2.imencode('.png', output_image)
    image = encoded_image.tobytes()
    _in_logger.info("Inference Compeleted")
    return Response(content=image, media_type="image/png")