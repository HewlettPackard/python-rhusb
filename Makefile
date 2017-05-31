all:

sdist:
	python setup.py sdist

install: sdist
	pip install dist/python-rhusb*tar.gz
	cp dist/python-rhusb*tar.gz /output