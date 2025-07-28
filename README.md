# AI Image Generator

A streamlined web application that generates images from text descriptions using Hugging Face's Stable Diffusion XL model. Built entirely with Streamlit for easy deployment and use.

## 🌟 Features

- **Text-to-Image Generation**: Create stunning images from text descriptions
- **Stable Diffusion XL**: Powered by state-of-the-art AI model
- **Customizable Parameters**:
  - Generate 1-4 images per prompt
  - Adjustable guidance scale (1.0-15.0)
  - Multiple image sizes (256x256, 512x512, 768x768)
- **User-Friendly Interface**: Clean, intuitive Streamlit interface
- **Real-time Progress**: Visual feedback during image generation
- **Cloud-Ready**: Designed for easy deployment on Streamlit Cloud

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Hugging Face account and API token ([Get one here](https://huggingface.co/settings/tokens))

### Local Installation

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd ai-image-generator
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up your Hugging Face token**:
   - Create a `.env` file in the project root:
   ```env
   HF_TOKEN=your_huggingface_token_here
   ```

4. **Run the application**:
```bash
streamlit run app.py
```

5. **Open your browser** and go to `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Deploy your app**:
   - Connect your GitHub account
   - Select this repository
   - Set the main file path to `app.py`

4. **Add your secrets**:
   - In the Streamlit Cloud dashboard, go to your app settings
   - Add a new secret: `HF_TOKEN = "your_huggingface_token_here"`

5. **Deploy!** Your app will be live at `https://your-app-name.streamlit.app`

### Other Platforms

The app can also be deployed on:
- **Heroku**: Use the included `requirements.txt`
- **Railway**: Direct deployment from GitHub
- **Render**: Static site deployment

## 📖 Usage Guide

### Basic Usage
1. Enter a descriptive text prompt
2. Click "Generate Images"
3. Wait for your AI-generated images!

### Advanced Options
- **Number of Images**: Generate 1-4 variations
- **Guidance Scale**: Control how closely the AI follows your prompt
  - Lower (1-5): More creative, abstract results
  - Higher (10-15): Stricter adherence to prompt
- **Image Dimensions**: Choose from 256x256, 512x512, or 768x768 pixels

### Pro Tips for Better Results
- **Be specific**: "A red sports car in a futuristic city at sunset"
- **Include style keywords**: "photorealistic", "digital art", "oil painting"
- **Mention composition**: "close-up", "wide angle", "bird's eye view"
- **Describe lighting**: "soft lighting", "dramatic shadows", "golden hour"

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Stable Diffusion XL via Hugging Face Inference API
- **Image Processing**: PIL (Python Imaging Library)
- **Deployment**: Cloud-native, serverless architecture

### Key Components
- `app.py`: Main Streamlit application
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (local development)

### Performance Considerations
- Images are generated server-side and returned as base64
- Larger images and more images take longer to generate
- Guidance scale affects generation time slightly

## 🔧 Configuration

### Environment Variables
- `HF_TOKEN`: Your Hugging Face API token (required)

### Model Settings
- **Model**: `stabilityai/stable-diffusion-xl-base-1.0`
- **Default Size**: 512x512 pixels
- **Default Guidance**: 7.5
- **Negative Prompt**: Empty (can be customized in code)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test locally: `streamlit run app.py`
5. Commit changes: `git commit -am 'Add feature'`
6. Push to branch: `git push origin feature-name`
7. Submit a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for providing the Stable Diffusion XL model and inference API
- **Streamlit** for the amazing web framework
- **Stability AI** for the Stable Diffusion model

## 📞 Support

If you encounter any issues:

1. **Check your HF_TOKEN**: Make sure it's valid and properly set
2. **Review the logs**: Streamlit shows detailed error messages
3. **Try different prompts**: Some prompts may not work well
4. **Reduce image size**: If generation is slow or failing

For additional help, please open an issue on GitHub.

---

**Happy generating! 🎨✨**