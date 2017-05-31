FROM centos:7
ENV http_proxy http://proxy.houston.hpecorp.net:8088
ENV https_proxy http://proxy.houston.hpecorp.net:8088
ADD https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm /root
RUN yum install -y /root/epel-release-latest-7.noarch.rpm
RUN yum makecache fast
RUN yum install -y python python-pip python-setuptools
RUN pip install --upgrade pip
COPY . /usr/src/python-rhusb
RUN cd /usr/src/python-rhusb && python setup.py bdist && pip install .
