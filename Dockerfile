FROM python:3
WORKDIR /app
COPY hello.py /app/hello.py
CMD ["python", "/app/hello.py"]
