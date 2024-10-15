"""import Adafruit_DHT # type: ignore

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
if humidity is not None and temperature is not None:
    print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
else:
    print("Sensor failure. Check wiring.")"""

# def getTempHumidity():
#     import random
#     return random.randint(35,40), random.randint(50,70)

def getTempHumidity():
    import Adafruit_DHT
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is None and temperature is None:
        return(0,0)
    else:
        #print(round(temperature,2),round(humidity,2))
        return(round(temperature,2),round(humidity,2))