#Jonathan Allef Rodrigues
import dth
import marchine
import time
import urequests
from dth import DTH11
from marchine import Pin
import network

def conectaWifi (red, password):
    global miRed
    miRed = network.WLAN(network.STA_IF)
    if not miRed.isconnected():

       miRed.active(True)
       miRed.connect(red, password)
          print('Conectando', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():
             if (time.ticks_diff (time.time (), timeout) > 10):
                return False
    return True

sensorDHT = DHT11 (Pin(5))

 if conectaWifi ("Troco senha por cerveja", "incorreto"):

     print ("Conectado!")
     print('Dados da rede (IP/netmask/gw/DNS):', miRed.ifconfig())

     url = "https://api.thingspeak.com/update?api_key=V2YVBRV74KUVM2UI"
else:
       print ("Impossível conectar")
       miRed.active (False)

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

while True:
   d.measure()
   print("Temperatura={}°C Umidade={}%".format(d.temperature(), d.humidity()))
   response = urequests.get("https://api.thingspeak.com/update?api_key=V2YVBRV74KUVM2UI"+"&field1="+str(d.temperature())+"&field2="+str(d.humidity()))
   print(response.text)
   print (response.status_code)
   response.close ()
   if d.temperature() > 31 or d.humidity() > 70:
     r.value(1)
   else:
     r.value(0)
   time.sleep(5)



