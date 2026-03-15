FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl
COPY app/app.py .

# Create non-root user for better security
RUN useradd -m appuser   
USER appuser

EXPOSE 5000

CMD ["python3", "app.py"]
