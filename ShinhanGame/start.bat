@echo off
chcp 65001 > nul
echo.
echo ========================================
echo   Shinhan Sales Training Game
echo ========================================
echo.
echo Browser: http://localhost:8501
echo Press Ctrl+C to stop
echo.
streamlit run app.py --server.port 8501
pause
