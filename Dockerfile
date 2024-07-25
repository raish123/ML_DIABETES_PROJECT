FROM python:3.11-slim-buster
WORKDIR /storage
COPY . /storage/
RUN  pip install -r requirements.txt
RUN apt-get update -y && apt-get install awscli -y
CMD ["python3","application.py"]