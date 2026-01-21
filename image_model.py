import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import uuid
import os

MODEL_ID = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)
pipe = pipe.to("cpu")  # change to "cuda" if GPU available

OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image(prompt: str) -> str:
    image = pipe(prompt).images[0]

    filename = f"{uuid.uuid4().hex}.png"
    path = os.path.join(OUTPUT_DIR, filename)

    image.save(path)
    return path
