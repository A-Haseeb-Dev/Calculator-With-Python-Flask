@echo off
echo Initializing environment...

REM Check if venv exists
IF NOT EXIST venv (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate

REM Install Flask if missing
echo Installing dependencies...
pip install flask >nul 2>&1

echo.
echo Starting Flask Calculator...
echo Open http://127.0.0.1:5000/ in your browser.
echo.

python app.py

pause
