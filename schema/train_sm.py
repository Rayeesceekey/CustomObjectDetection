from pydantic import BaseModel


class TrainData(BaseModel):
    yaml_file_path: str
    yolo_weight_file: str
    epochs :int

