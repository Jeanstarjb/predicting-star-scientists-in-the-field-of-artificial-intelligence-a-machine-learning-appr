FROM python:3.9-slim

WORKDIR /app

COPY ml_model/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ml_model .

CMD ["python", "train.py"]