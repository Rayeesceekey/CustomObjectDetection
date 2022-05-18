from pydantic import BaseModel
from typing import Optional

class InputDataImg(BaseModel):
    image_path :str
    yaml_file_path : str
    model_path : str
    use_pretrained : Optional[bool] = False

class InputDataPath(BaseModel):
    image_path :str
    yaml_file_path : str
    model_path : str