# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Expose Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "App_master/app.py", "--server.port=8501", "--server.enableCORS=false"]
