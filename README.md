# Boilerplate for MicroPython on ESP32 with WebREPL

# Configuration
- Copy `webrepl_cfg.example.py` to `webrepl_cfg.py`
- Edit `webrepl_cfg.py` to set your passwords and SSID

# Requirements
## Download the firmware
[Download MicroPython firmware for ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/)
## Create Virtual Environment and install requirements
```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
wget https://raw.githubusercontent.com/micropython/micropython/refs/heads/master/tools/pyboard.py -O venv/bin/pyboard.py
chmod +x venv/bin/pyboard.py
```

# Install on ESP32
```bash
FIRMWARE="${HOME}/Downloads/ESP32_GENERIC-20241025-v1.24.0.bin"
export PYBOARD_DEVICE="/dev/tty.usbserial-021R2JF2"

esptool.py --chip esp32 --port "${PYBOARD_DEVICE}" write_flash -z --erase-all --compress 0x1000 "${FIRMWARE}"

sleep 5 # wait for the ESP32 to reboot

pyboard.py  -f  cp webrepl_cfg.py :
pyboard.py  -f  cp boot.py :

screen  "${PYBOARD_DEVICE}"  115200
```
Press the "Reset" button on the ESP32 to start the REPL.

Notes:
- Press `Ctrl-A` then `Ctrl-\` to exit `screen`
- The `PYBOARD_DEVICE` environment variable is used by the `pyboard.py` script as serial port setting. 
