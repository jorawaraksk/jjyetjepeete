FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

COPY . .

RUN pip install -r requirements.txt

CMD ["bash", "run.sh"]
