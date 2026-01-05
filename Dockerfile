FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Set environment variable so Python can find the src folder
ENV PYTHONPATH=/app/src

# Run the app
CMD ["python", "src/app.py"]