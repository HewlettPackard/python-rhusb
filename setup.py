"""
Python module which abstracts the USB-Serial interface to the RH-USB sensor

Copyright (C) 2017, Hewlett-Packard Development Company
Author: Dave Brookshire <dsb@hpe.com>

"""
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='python-rhusb',
    version='1.0',
    packages=[''],
    url='https://github.com/brookshire/python-rhusb',
    license='Apache License Version 2.0',
    author='Dave Brookshire',
    author_email='dsb@hpe.com',
    description='Module which abstracts the USB-Serial Interface to the RH-USB sensor',
    long_description='Module which abstracts the USB-Serial Interface to the RH-USB sensor',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: IoT :: Sensors',
        'License:: Apache License Version 2.0',
        'Programming Language :: Python 2.7',
    ],
    keywords='sensor sensors rh-usb temperature humidity',
    py_modules=["rhusb"],
)
