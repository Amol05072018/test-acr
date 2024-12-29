FROM python:3.9-slim
RUN pip install streamlit numpy matplotlib
COPY . .
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=8051", "--server.address=0.0.0.0"]