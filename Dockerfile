FROM python:3.11-slim

WORKDIR /app

COPY santhosh/app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY santhosh/app/ /app

EXPOSE 5000

CMD ["python", "app.py"]
