# Install GPS Modul on Raspberry Pi 3 

## Requirements
 * Raspberry Pi 3
 * Raspbian Stretch Lite
 * AZ-Delivery NEO-6M GPS Modul

## Configure the services
```console
sudo nano /boot/cmdline.txt
```

Replace the existing line with the following:
```console
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
```

## Update boot config 
```console
sudo nano /boot/config.txt
```

Add or uncomment these lines (search with [strg]+[w]):
```console
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
init_uart_baud=9600
```

## Install Git and Python 
```console
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install libssl-dev libffi-dev gpsd gpsd-clients minicom git python3 python3-nmea2 python3-dev python3-pip python3-serial -y
```

## Configure baud rate
Reboot your device with `sudo shutdown -r now`.

Configure baud rate:
```console
stty -F /dev/ttyAMA0 9600
```

## Connect to AMA0
Kill the process and update gpsd:
```console
sudo killall gpsd
sudo nano /etc/default/gpsd
```

Update the following line:
```console
DEVICES="/dev/ttyAMA0"
```

## Restart services
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket 

## Test
### Read AMA0
```console
cgps -s
```

### Python example
```console
cd /tmp
git clone git@github.com:plakna/raspberry-pi-gps-neo-6m.git
cd raspberry-pi-gps-neo-6m/examples

python3 gps.py
```