FROM tensorflow/tensorflow:2.6.0-gpu-jupyter

RUN apt-get -yq update;apt-get install -yq vim wget
RUN pip3 install imageio==2.6.0

WORKDIR /opt
COPY hello.py .
COPY hello.sh .

COPY requirements.txt .
RUN pip3 install -r requirements.txt
