FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# RUN apt-get update

COPY ./. /app

WORKDIR /app

RUN pip install -q --upgrade pip setuptools wheel

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -qr requirements.txt
