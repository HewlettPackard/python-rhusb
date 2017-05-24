# python-rhusb

This library provides a pure Python interface to the
Omega RH-USB temperature/humidity sensor.The device 
includes a USB-Serial interface which is used to send 
commands and receive input from the device.

More information on this device is available at
http://www.omega.com/pptst/RH-USB.html

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The python-rhusb library uses the pyserial library.

```
pip install pyserial
```

### Installing

From Source:

```
$ git clone https://github.com/HewlettPackard/python-rhusb.git
$ cd python-rhusb
$ python setup.py install --user # to install in the user directory (~/.local)
$ python setup.py install        # to install globally
```

Using PIP:

```
$ git clone https://github.com/HewlettPackard/python-rhusb.git
$ cd python-rhusb
$ pip install .
```

From Pypi:

TBD

## Running the tests

TBD

## Built With

TBD

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Dave Brookshire** - *Initial work* - [HPE](https://github.com/brookshire)

## License

This project is licensed under the Apache 2.0 License- see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* http://stackoverflow.com/questions/25662489/how-to-write-on-serial-port-in-python-that-ttyusb0-will-be-interpreted-commands
* http://www.roman10.net/serial-port-communication-in-python/
* http://www.brettdangerfield.com/post/raspberrypi_tempature_monitor_project/