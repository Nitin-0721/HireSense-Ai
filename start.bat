@echo off

start cmd /k "cd /d %~dp0backend && venv\Scripts\activate && uvicorn app:app --reload --host 127.0.0.1 --port 8000"

timeout /t 3 /nobreak >nul

start cmd /k "cd /d %~dp0backend && venv\Scripts\activate && streamlit run ..\frontend\frontend.py"