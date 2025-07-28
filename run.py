import subprocess
import sys
import os
from time import sleep

def run_backend():
    backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Backend")
    os.chdir(backend_dir)
    subprocess.Popen([sys.executable, "main.py"])

def run_frontend():
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
    os.chdir(frontend_dir)
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "clients.py"])

if __name__ == "__main__":
    print("Starting the AI Image Generator...")
    print("\n1. Starting Backend server...")
    run_backend()
    
    # Wait for backend to start
    print("Waiting for backend to initialize...")
    sleep(3)
    
    print("\n2. Starting Frontend application...")
    run_frontend()
    
    print("\nApplication started successfully!")
    print("- Backend is running on: http://localhost:8000")
    print("- Frontend is running on: http://localhost:8501")
    print("\nPress Ctrl+C to stop both servers")
