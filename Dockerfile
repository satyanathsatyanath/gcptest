from python:3.11-slim

WORKDIR /app

COPY requrirements.txt .

RUN pip install --no-cache-dir -r requrirements.txt

COPY app.py .

ENV PORT=8000

CMD["python", "app.py"]