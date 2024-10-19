def getTempHumidity():
    import Adafruit_DHT
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is None and temperature is None:
        return(0,0)
    else:
        return(round(temperature,2),round(humidity,2))