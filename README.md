# Boilerplate for MicroPython on ESP32 with WebREPL
Will probably work on other boards like ESP8266, but I haven't tested it.

# Configuration
- Copy `webrepl_cfg.example.py` to `webrepl_cfg.py`
- Edit `webrepl_cfg.py` to set your passwords and SSID

# ESP32
[Download MicroPython firmware for ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/) 
```bash
FIRMWARE="~/Downloads/ESP32_GENERIC-20241025-v1.24.0.bin"
export PYBOARD_DEVICE="/dev/tty.usbserial-021R2JF2"

esptool.py --chip esp32 --port "${PYBOARD_DEVICE}" write_flash -z --erase-all --compress 0x1000 "${FIRMWARE}"

./pyboard.py -f cp webrepl_cfg.py :
./pyboard.py -f cp boot.py :

screen $PYBOARD_DEVICE 115200
```
The `PYBOARD_DEVICE` environment variable is used by the `pyboard.py` script as serial port setting. 
