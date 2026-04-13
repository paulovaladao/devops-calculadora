FROM python:3.10-slim

WORKDIR /app

COPY calculadora.py .

CMD ["python", "calculadora.py"]