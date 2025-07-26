import os, io, base64
from huggingface_hub import InferenceClient, login
from dotenv import load_dotenv


load_dotenv(override=True)  
token = os.getenv("HF_TOKEN")  
if not token:
    print("Warning: HF_TOKEN not found in environment variables")
    print("Current working directory:", os.getcwd())
    print("Looking for .env file in:", os.path.abspath('.'))
    raise ValueError("Please set HF_TOKEN in your .env file")


login(token=token)

print("Token loaded successfully")  


client = InferenceClient(token=token)

def generate(prompt, num_images, guidance_scale, height, width):
    results = []
    for _ in range(num_images):
        # Generate image using the inference client
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
