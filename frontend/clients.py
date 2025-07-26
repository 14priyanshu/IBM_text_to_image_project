import streamlit as st
import requests
import time

st.set_page_config(page_title="AI Image Generator")
st.title("🖼️ AI Image Generator")


status_container = st.empty()

prompt = st.text_input("Enter a prompt")
options = st.expander("Advanced options")
with options:
    num_images = st.number_input("Number of images", min_value=1, max_value=4, value=1)
    guidance = st.slider("Guidance scale", 1.0, 15.0, 7.5)
    width = st.select_slider("Width", options=[256, 512, 768], value=512)
    height = st.select_slider("Height", options=[256, 512, 768], value=512)


try:
    response = requests.get("http://localhost:8000")
    # if response.status_code == 200:
        # status_container.success("✅ Backend is connected")
except:
    status_container.error("❌ Backend is not running. Please start the backend server first.")

if st.button("Generate"):
    if not prompt:
        st.error("Please enter a prompt.")
        st.stop()

    try:
        
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        
        progress_text.text("🎨 Starting image generation...")
        progress_bar.progress(10)
        
        with st.spinner():
          
            response = requests.post(
                "http://localhost:8000/generate",
                json={
                    "prompt": prompt,
                    "num_images": num_images,
                    "guidance_scale": guidance,
                    "width": width,
                    "height": height
                },
                timeout=90 
            )
            
            progress_bar.progress(50)
            progress_text.text("⚡ Processing the generated images...")
            
            if response.status_code == 200:
                res = response.json()
                progress_bar.progress(90)
                progress_text.text("✨ Almost done...")
                
               
                for img in res["images"]:
                    st.image(img)
                
              
                progress_bar.progress(100)
                progress_text.empty()
                st.success("✨ Images generated successfully!")
            else:
                progress_bar.empty()
                progress_text.empty()
                st.error(f"Server error: {response.text}")
                
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend server. Please make sure it's running on http://localhost:8000")
        st.info("To start the backend server, run: uvicorn main:app --reload --host 0.0.0.0 --port 8000")
    except requests.exceptions.Timeout:
        st.error("⌛ The request timed out. The image generation is taking longer than expected.")
        st.info("Try reducing the number of images or image size.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
