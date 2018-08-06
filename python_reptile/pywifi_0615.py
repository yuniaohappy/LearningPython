import pywifi
import time

def gic():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()#断开wifi连接

    profile = pywifi.Profile()
    profile.ssid = "LP519"
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = "LP519@lpsddz"
#    ifaces.remove_all_network_profile()
    tmp_profile = ifaces.add_network_profile(profile)

    ifaces.connect(tmp_profile)
    time.sleep(1)
    isok = True
    print(ifaces.status(), pywifi.const.IFACE_CONNECTED)
    if ifaces.status() == pywifi.const.IFACE_CONNECTED:
        print("已连接")

    else:
        print("未连接")

gic()