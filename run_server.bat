@echo off
venv\Scripts\activate
uvicorn app.main:app --reload
pause
