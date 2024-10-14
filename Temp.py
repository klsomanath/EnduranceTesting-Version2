def getTemp1():
    import max6675
    cs = 8
    sck = 11
    so = 9
    max6675.set_pin(cs, sck, so, 1)
    try:
        a = max6675.read_temp(cs)
        print(a)
        return a
    except KeyboardInterrupt:
        return 0
        pass
def getTemp2():
    import max6675
    cs = 7
    sck = 11
    so = 9
    max6675.set_pin(cs, sck, so, 1)
    try:
        a = max6675.read_temp(cs)
        print(a)
        return a
    except KeyboardInterrupt:
        return 0
        pass