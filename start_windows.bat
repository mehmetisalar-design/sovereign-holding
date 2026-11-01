@echo off
setlocal
cd /d "%~dp0"
echo ========================================
echo Atelier Home - Windows startup
echo ========================================
where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo ERROR: Python was not found. Install Python 3.11 or newer and enable Add Python to PATH.
    pause
    exit /b 1
  )
  set PYTHON=python
) else (
  set PYTHON=py -3
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PYTHON% -m venv .venv
  if errorlevel 1 (echo ERROR: Could not create virtual environment.& pause & exit /b 1)
)
call ".venv\Scripts\activate.bat"
if errorlevel 1 (echo ERROR: Could not activate virtual environment.& pause & exit /b 1)
echo Installing/updating dependencies...
python -m pip install --upgrade pip
if errorlevel 1 (echo ERROR: pip upgrade failed. Check your internet connection.& pause & exit /b 1)
pip install -r requirements.txt
if errorlevel 1 (echo ERROR: Dependency installation failed.& pause & exit /b 1)
if not exist ".env" (
  copy ".env.example" ".env" >nul
  echo Created .env from template. Edit SECRET_KEY before using beyond local development.
)
echo Starting Atelier Home at http://127.0.0.1:5000
echo Press Ctrl+C to stop the server.
python run.py
if errorlevel 1 echo ERROR: Server stopped with an error. Read the traceback above.
pause
