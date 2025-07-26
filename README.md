# AI Image Generator

This project is a web application that generates images from text descriptions using Hugging Face's Stable Diffusion model. It consists of a FastAPI backend and a Streamlit frontend.

## Features

- Text-to-image generation using Stable Diffusion XL
- User-friendly web interface
- Customizable image generation parameters:
  - Multiple images per prompt (1-4)
  - Adjustable guidance scale
  - Configurable image dimensions
- Real-time generation progress tracking
- Base64 image encoding for seamless display

## Tech Stack

- **Backend:**
  - FastAPI (Python web framework)
  - Hugging Face Hub (AI model integration)
  - Python-dotenv (environment management)

- **Frontend:**
  - Streamlit (UI framework)
  - Requests (HTTP client)

## Setup

### Prerequisites

- Python 3.8 or higher
- Hugging Face account and API token
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/14priyanshu/IBM_text_to_image_project.git
cd IBM_text_to_image_project
```

2. Set up the backend:
```bash
cd Backend
pip install -r requirements.txt
```

3. Create a `.env` file in the Backend directory:
```env
HF_TOKEN=your_huggingface_token_here
```

4. Set up the frontend:
```bash
cd ../frontend
pip install -r requirements.txt
```

## Running the Application

1. Start the backend server:
```bash
cd Backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Start the frontend (in a new terminal):
```bash
cd frontend
streamlit run clients.py
```

3. Open your browser and go to http://localhost:8501

## Usage

1. Enter a text prompt describing the image you want to generate
2. (Optional) Adjust advanced settings:
   - Number of images to generate
   - Guidance scale (how closely to follow the prompt)
   - Image dimensions
3. Click "Generate" and wait for your images

## Configuration Options

- **Image Size:** 256x256, 512x512, or 768x768 pixels
- **Number of Images:** 1-4 images per generation
- **Guidance Scale:** 1.0-15.0 (higher values = closer adherence to prompt)

## Deployment

The application can be deployed to Vercel:

1. Create a Vercel account
2. Connect your GitHub repository
3. Set the environment variable `HF_TOKEN` in Vercel dashboard
4. Deploy using the Vercel configuration provided

## Project Structure

```
IBM_project_text_to_image/
├── Backend/
│   ├── main.py           # FastAPI application
│   ├── service.py        # Image generation logic
│   ├── schemas.py        # Data models
│   └── requirements.txt  # Backend dependencies
├── frontend/
│   ├── clients.py        # Streamlit interface
│   └── requirements.txt  # Frontend dependencies
└── vercel.json          # Vercel deployment configuration
```

## Security

- The `.env` file is excluded from version control
- Hugging Face token is stored securely as an environment variable
- CORS is configured for secure communication between frontend and backend

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for providing the Stable Diffusion model
- Streamlit for the amazing UI framework
- FastAPI for the efficient backend framework
