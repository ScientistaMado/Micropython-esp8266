import network
import gc

gc.collect()

SSID = 'YOUR SSID'
PASSWORD = 'YOUR PASS'
URL_API = 'YOUR URL API'


def connectWifi(ssid, password):

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        print('conectando')

    print(f'Conectado con éxito a {ssid}')

    oled.fill(0)
    oled.text("Conectado", 10, 10)
    oled.show()


def fetchApi(api_url, timeout=10):
    try:
        response = requests.get(api_url, timeout=timeout)

        if response.status_code == 200:
            return response.text
        else:
            print('Error en la solicitud. Código de respuesta HTTP:',
                  response.status_code)
            return None

    except Exception as e:
        print('Error en la solicitud:', str(e))
        return None
