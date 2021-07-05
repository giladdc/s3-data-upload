FROM ubuntu:18.04
RUN apt update && apt install -y python3 python3-pip
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 main.py

