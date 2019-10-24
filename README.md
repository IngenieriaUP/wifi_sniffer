# wifi_sniffer
Wifi devices sniffer in python

## Quick Start

1. Connect TP-Link TL-WN7222N

2. Open terminal and run:

```sh
$ sudo apt-get install net-tools tshark python3-tk
$ iwconfig
```
3. Get the device code and then run:

```sh
$ ifconfig {device code} down
$ sudo iwconfig {device code} mode monitor
$ sudo ifconfig {device code} up
```

4. Create virtualenv (optional) and then install python requirements:

```sh
(.env) $ pip install -r requirements.txt
```

5. Run sniffer.py as superuser:

```sh
$ sudo su
(.env) $ python sniffer.py
```
