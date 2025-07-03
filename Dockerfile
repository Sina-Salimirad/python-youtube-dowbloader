FROM python:3.15.5-slim


# Install ffmpeg (Dependence)
RUN apt-get update && apt-get install ffmpeg -y

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "main.py"]
