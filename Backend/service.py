import os, io, base64
from huggingface_hub import InferenceClient, login
from dotenv import load_dotenv



load_dotenv(override=True)


token = os.getenv("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")

if not token:
    raise ValueError("No HuggingFace token found. Please set HF_TOKEN in environment variables or .env file")


login(token=token)

print("Token loaded successfully")  


client = InferenceClient(token=token)

def generate(prompt, num_images, guidance_scale, height, width):
    results = []
    for _ in range(num_images):
       
        image = client.text_to_image(
            prompt,
            negative_prompt="",
            model="stabilityai/stable-diffusion-xl-base-1.0",
            width=width,
            height=height,
            guidance_scale=guidance_scale
        )
        
        
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        results.append(f"data:image/png;base64,{b64}")
    return results
