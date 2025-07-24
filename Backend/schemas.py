from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str
    num_images: int = 1
    guidance_scale: float = 7.5
    height: int = 512
    width: int = 512
