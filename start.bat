@echo off
title HireSense-AI

start "HireSense Backend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && uvicorn app:app --reload --host 127.0.0.1 --port 8000"

timeout /t 3 /nobreak >nul

start "HireSense Frontend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && streamlit run ..\frontend\frontend.py"

exit