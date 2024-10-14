def getPress1():
    import time
    import board
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
    val=chan.value
    volt=chan.voltage
    #print(volt)
    current12 = (volt * 10)
    pressure12 = round(((current12 - 4) / (20 - 0)) * 40,2)
    print(f"Pressure: {pressure12} bar")
    #time.sleep(1)
    return pressure12
def getPress2():
    import time
    import board
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
    val=chan.value
    volt=chan.voltage
    #print(volt)
    current12 = (volt * 10)
    pressure12 = round(((current12 - 4) / (20 - 0)) * 40,2)
    print(f"Pressure: {pressure12} bar")
    return pressure12