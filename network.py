# PORT=/dev/tty.usbserial-021R2JF2
# esptool.py --chip esp32 --port "${PORT}" write_flash -z --erase-all --compress 0x1000 ~/Downloads/ESP32_GENERIC-20241025-v1.24.0.bin

# screen $PORT 115200

# export PYBOARD_DEVICE=/dev/tty.usbserial-021R2JF2
# ./pyboard.py network.py

import network
import time

def do_connect(ssid, pwd, hard_reset=True):
    interface = network.WLAN(network.STA_IF)

    # Stage zero: if credential are null disconnect
    if not pwd or not ssid :
        print('Disconnecting')
        interface.active(False)
        return None

    # Stage one: check for default connection
    for t in range(0, 120):
        if interface.isconnected():
            print('Got connected, my IP address:', interface.ifconfig()[0])
            return interface
        time.sleep_ms(200)
        # Stage two: if not yet connected and after a hard reset activate and connect
        if t == 60 and hard_reset:
            interface.active(True)
            interface.connect(ssid, pwd)

    # No way we are not connected
    print('Cant connect to ', ssid)
    return None


do_connect('GRS-IOT', 'youremindme')

