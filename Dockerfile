FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

COPY ./test ./test

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


