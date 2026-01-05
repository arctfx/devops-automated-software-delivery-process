FROM python:3.12-slim

# Create a non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and change ownership to the new user
COPY src/ ./src/
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

ENV PYTHONPATH=/app/src

CMD ["python", "src/app.py"]