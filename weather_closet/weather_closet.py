import network
import esp
import gc
import time
import sh1106
import framebuf
import urequests as requests
import ure as re
from machine import Pin, I2C


esp.osdebug(None)
gc.collect()

SSID = 'Natalia_Mi'
PASSWORD = '188804115'
URL_API = 'http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=tmmvlzsz8496'



def connectWifi(ssid, password):
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid,password)
    
    oled.text("Conectando", 10,10)
    oled.show()
    dot = 10
    
    while not station.isconnected():
        print('conectando')
        oled.text(".", dot+6,10)
        oled.show()
        time.sleep(1)

    print(f'Conectado con éxito a {ssid}')
    
    oled.fill(0)
    oled.text("Conectado", 10,10)
    oled.show()


def fetchApi(api_url, timeout=10):
    try:
        response = requests.get(api_url, timeout=timeout)
        
        if response.status_code == 200:
            return response.text
        else:
            print('Error en la solicitud. Código de respuesta HTTP:', response.status_code)
            return None
        
    except Exception as e:
        print('Error en la solicitud:', str(e))
        return None
    

def getVar(report, tag_element):
    
        start = report.find(tag_element)
        
        if tag == "Símbolo del tiempo":
            var = re.search(r'id="(.*?)"', report[start:])
        else:
            var = re.search(r'value="(.*?)"', report[start:])
            
        return var.group(1)


def openIcon(icon_id):
    
    with open(f'icons/{icon_id}.pbm', "rb") as file:
        file.readline()
        xy = file.readline()
        x = int(xy.split()[0])
        y = int(xy.split()[1])
        icon = bytearray(file.read())
    
    return framebuf.FrameBuffer(icon, x, y, framebuf.MONO_HLSB)


def showInOled(data):
    oled.fill(0)
    
    day = data["Día"]
    day_x = int((128 - (len(day)*8))/2)
    
    if day == "Miércoles":
        day = "Miercoles"
    if day == "Sábado":
        day = "Sábado"
    
    oled.text(day, day_x,2)
    
    t = f'{data["Temperatura Mínima"]}-{data["Temperatura Máxima"]}C'
    t_x = int((128 - (len(t)*8))/2)

    oled.text(t, t_x, 18)

    
    icon_id = data["Símbolo del tiempo"]
    oled.blit(openIcon(icon_id), 48, 32)
    
    oled.show()



i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
oled.sleep(False)
oled.fill(0)

connectWifi(SSID, PASSWORD)
data_api = fetchApi(URL_API)

data_dict = {"Temperatura Mínima": "",
             "Temperatura Máxima": "",
             "Día": "",
             "Símbolo del tiempo": ""}

for tag in data_dict:
    data_dict[tag] = getVar(data_api, tag)
    

showInOled(data_dict)
print(data_dict)
















