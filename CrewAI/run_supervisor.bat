@echo off
REM Agency Supervisor - Quick Chat

cd /d "%~dp0"

echo ============================================
echo   Agency Supervisor - 150+ Agents Chat
echo ============================================
echo.

REM Set API keys
set GROQ_API_KEY=your_groq_api_key_here
set GEMINI_API_KEY=your_gemini_api_key_here

echo API Keys loaded.
echo.

REM Run the chat
python src\agency_crew\main.py

pause
