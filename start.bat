@echo off
title HireSense-AI Launcher

echo ==============================
echo      HireSense-AI Starting
echo ==============================
echo.

echo Starting Backend...
start "HireSense Backend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && uvicorn app:app --reload --host 127.0.0.1 --port 8000"

timeout /t 3 /nobreak

echo Starting Frontend...
start "HireSense Frontend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && streamlit run ..\frontend\frontend.py"

echo.
echo HireSense-AI is starting...
echo.
pause