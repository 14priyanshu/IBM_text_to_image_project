@echo off
echo Starting Backend Server...
cd Backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000
