FROM python:3.11-slim

WORKDIR /app

RUN pip install pydantic==2.6.4

COPY . .

CMD ["python", "tasks.py"]
