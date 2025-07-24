import os, io, base64
from huggingface_hub import InferenceClient, login
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)  # Force reload environment variables
token = os.getenv("HF_TOKEN")  # Changed to match the variable name in .env file
if not token:
    print("Warning: HF_TOKEN not found in environment variables")
    print("Current working directory:", os.getcwd())
    print("Looking for .env file in:", os.path.abspath('.'))
    raise ValueError("Please set HF_TOKEN in your .env file")

# Login to Hugging Face
login(token=token)

print("Token loaded successfully")  # Debug message

# Initialize the Hugging Face Inference Client
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
        
        # Convert the image to base64
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        results.append(f"data:image/png;base64,{b64}")
    return results
