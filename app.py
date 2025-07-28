import streamlit as st
import os
import io
import base64
from huggingface_hub import InferenceClient, login
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

st.set_page_config(page_title="AI Image Generator")
st.title("🖼️ AI Image Generator")

# Initialize HuggingFace client
@st.cache_resource
def get_hf_client():
    """Initialize and cache the HuggingFace client"""
    try:
        # Try to get token from Streamlit secrets first, then environment
        token = st.secrets.get("HF_TOKEN") or os.getenv("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        
        if not token:
            st.error("❌ No HuggingFace token found. Please set HF_TOKEN in Streamlit secrets or environment variables.")
            st.stop()
        
        # Login to HuggingFace
        login(token=token)
        
        # Create and return client
        client = InferenceClient(token=token)
        st.success("✅ Successfully connected to HuggingFace!")
        return client
        
    except Exception as e:
        st.error(f"❌ Error initializing HuggingFace client: {str(e)}")
        st.stop()

def generate_images(client, prompt, num_images, guidance_scale, height, width):
    """Generate images using HuggingFace Stable Diffusion"""
    results = []
    
    # Create progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        for i in range(num_images):
            status_text.text(f"🎨 Generating image {i+1} of {num_images}...")
            progress_bar.progress((i) / num_images)
            
            # Generate image
            image = client.text_to_image(
                prompt,
                negative_prompt="",
                model="stabilityai/stable-diffusion-xl-base-1.0",
                width=width,
                height=height,
                guidance_scale=guidance_scale
            )
            
            # Convert to base64
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            b64 = base64.b64encode(buf.getvalue()).decode()
            results.append(f"data:image/png;base64,{b64}")
            
            # Update progress
            progress_bar.progress((i + 1) / num_images)
        
        status_text.text("✨ All images generated successfully!")
        return results
        
    except Exception as e:
        status_text.text("")
        progress_bar.empty()
        raise e

# Initialize the HuggingFace client
client = get_hf_client()

# UI Components
prompt = st.text_input("Enter a prompt", placeholder="A beautiful sunset over mountains...")

# Advanced options
with st.expander("🔧 Advanced Options"):
    col1, col2 = st.columns(2)
    
    with col1:
        num_images = st.number_input("Number of images", min_value=1, max_value=4, value=1)
        guidance = st.slider("Guidance scale", 1.0, 15.0, 7.5, 
                           help="Higher values make the AI follow your prompt more closely")
    
    with col2:
        width = st.select_slider("Width", options=[256, 512, 768], value=512)
        height = st.select_slider("Height", options=[256, 512, 768], value=512)

# Generate button
if st.button("🚀 Generate Images", type="primary"):
    if not prompt.strip():
        st.error("❌ Please enter a prompt to generate images.")
        st.stop()
    
    try:
        with st.spinner("🎨 Creating your masterpiece..."):
            # Generate images
            images = generate_images(client, prompt, num_images, guidance, height, width)
            
            # Display results
            st.success(f"✨ Successfully generated {len(images)} image(s)!")
            
            # Show images in columns for better layout
            if len(images) == 1:
                st.image(images[0], caption=f"Generated: {prompt}")
            else:
                cols = st.columns(min(len(images), 2))
                for idx, img in enumerate(images):
                    with cols[idx % 2]:
                        st.image(img, caption=f"Image {idx+1}: {prompt}")
                        
    except Exception as e:
        st.error(f"❌ Error generating images: {str(e)}")
        st.info("💡 Try reducing the number of images or adjusting the image size if the error persists.")

# Add some helpful information
with st.sidebar:
    st.markdown("### 📖 How to use")
    st.markdown("""
    1. **Enter a prompt** describing the image you want
    2. **Adjust settings** (optional) in Advanced Options
    3. **Click Generate** and wait for your images!
    
    ### 💡 Tips for better results
    - Be specific and descriptive
    - Include style keywords (e.g., "photorealistic", "digital art")
    - Mention lighting, colors, and composition
    
    ### ⚙️ Settings Guide
    - **Guidance Scale**: Higher = closer to prompt
    - **Image Size**: Larger = more detail, slower generation
    - **Number of Images**: Generate multiple variations
    """)
    
    st.markdown("---")
    st.markdown("**Powered by Stable Diffusion XL** 🤖")