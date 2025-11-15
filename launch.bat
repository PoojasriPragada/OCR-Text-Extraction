@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Starting OCR Streamlit App...
streamlit run app.py

pause