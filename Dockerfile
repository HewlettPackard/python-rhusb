FROM ubuntu:latest
ENV http_proxy http://proxy.houston.hpecorp.net:8088
ENV https_proxy http://proxy.houston.hpecorp.net:8088
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python34 python34-pip
COPY . /usr/src/python-rhusb
RUN cd /usr/src/python-rhusb && python setup.py bdist && pip install .
