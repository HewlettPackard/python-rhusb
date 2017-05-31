FROM python:latest
ENV http_proxy http://proxy.houston.hpecorp.net:8088
ENV https_proxy http://proxy.houston.hpecorp.net:8088
#RUN yum install -y python python-pip python-setuptools
COPY . /usr/src/python-rhusb
#RUN cd /usr/src/python-rhusb && python setup.py sdist && pip install dist/python-rhusb*.tar.gz
#CMD cp /usr/src/python-rhusb/dist/python-rhusb*.tar.gz /output
CMD ["python", "setup.py", "sdist", ";", "ls", "dist"]