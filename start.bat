@echo off
title HireSense-AI

echo Starting Backend Server...
start "HireSense Backend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && uvicorn app:app --host 127.0.0.1 --port 8000"

echo Waiting for backend to finish loading models (this can take a while)...
set /a tries=0

:wait
powershell -NoProfile -Command "try { Invoke-WebRequest -Uri http://127.0.0.1:8000/docs -UseBasicParsing -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
if %errorlevel%==0 goto ready
set /a tries+=1
if %tries% GEQ 90 (
    echo.
    echo Backend did not start within 3 minutes.
    echo Check the "HireSense Backend" window for the error.
    pause
    exit /b 1
)
timeout /t 2 /nobreak >nul
goto wait

:ready
echo Backend is up. Starting Frontend...
start "HireSense Frontend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && streamlit run ..\frontend\frontend.py"
exit