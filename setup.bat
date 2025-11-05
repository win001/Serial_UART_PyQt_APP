@echo off
echo ========================================
echo UART Serial Terminal - Setup Script
echo ========================================
echo.

REM Check if virtual environment exists
if exist "venv" (
    echo Virtual environment already exists.
    echo.
) else (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully.
    echo.
)

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the application:
echo   1. Activate the virtual environment: venv\Scripts\activate
echo   2. Run the application: python serial_terminal.py
echo.
echo Or simply run: run.bat
echo.
pause
