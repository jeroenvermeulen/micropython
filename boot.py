# export PYBOARD_DEVICE=/dev/tty.usbserial-021R2JF2
# esptool.py --chip esp32 --port "${PYBOARD_DEVICE}" write_flash -z --erase-all --compress 0x1000 ~/Downloads/ESP32_GENERIC-20241025-v1.24.0.bin

# ./pyboard.py -f cp webrepl_cfg.py :
# ./pyboard.py -f cp boot.py :

# screen $PYBOARD_DEVICE 115200

import network
import time
import webrepl
import esp
import webrepl_cfg

def do_connect(wifi_ssid, wifi_password):
    # Wireless config : Station mode
    station = network.WLAN(network.STA_IF)
    station.active(True)

    # Connect to WiFi access point
    print(f"Connecting to {wifi_ssid}", end="")
    station.connect(wifi_ssid, wifi_password)
    while 1:
        print(".", end="")
        try:
            if station.isconnected():
                print("")
                break
        except OSError as e:
            pass
        time.sleep(.5)

    # Display connection details
    print("Connected!")
    print("My IP Address:", station.ifconfig()[0])

if __name__ == "__main__":
    print("Booting...")
    esp.osdebug(None)
    interface = do_connect(webrepl_cfg.WIFI_SSID, webrepl_cfg.WIFI_PASS)
    webrepl.start()
    print("Finished boot.")
