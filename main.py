import network
import sgota

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('mate20raph', '12346789')
    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())


sgota.update("https://github.com/tremblayraphael29/esp32_update_essai/commits?path=code/example.py")
