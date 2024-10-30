def EVXX(now,i,ev08c,ev09c,ev13c):
    import RPi.GPIO as GPIO
    import time,dataBase
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    ev08 = 17
    ev09 = 27
    ev13 = 22
    GPIO.setup(ev08, GPIO.OUT)
    GPIO.setup(ev09, GPIO.OUT)
    GPIO.setup(ev13, GPIO.OUT)

    GPIO.output(ev08,GPIO.HIGH)
    GPIO.output(ev09,GPIO.HIGH)
    GPIO.output(ev13,GPIO.HIGH)
    try:
        cycle_data=[]
        cycle_data.append(str(i+1))
        cycle_data.append(now)
        if i == 1:
            GPIO.output(ev08,GPIO.LOW)
            GPIO.output(ev09,GPIO.HIGH)
            GPIO.output(ev13,GPIO.HIGH)
            cycle_data.append(1)
            cycle_data.append(0)
            cycle_data.append(0)
            ev08c+=1
            time.sleep(0.5)
        if i == 2:
            GPIO.output(ev08,GPIO.LOW)
            GPIO.output(ev09,GPIO.HIGH)
            GPIO.output(ev13,GPIO.LOW)
            cycle_data.append(1)
            cycle_data.append(0)
            cycle_data.append(1)
            ev08c+=1
            ev13c+=1
            time.sleep(0.5)
        if i == 3:
            GPIO.output(ev08,GPIO.HIGH)
            GPIO.output(ev09,GPIO.HIGH)
            GPIO.output(ev13,GPIO.HIGH)
            cycle_data.append(0)
            cycle_data.append(0)
            cycle_data.append(0)
            time.sleep(0.5)
        if i == 4:
            GPIO.output(ev08,GPIO.HIGH)
            GPIO.output(ev09,GPIO.LOW)
            GPIO.output(ev13,GPIO.HIGH)
            cycle_data.append(0)
            cycle_data.append(1)
            cycle_data.append(0)
            ev09c+=1
            time.sleep(0.5)
        if i == 5:
            GPIO.output(ev08,GPIO.HIGH)
            GPIO.output(ev09,GPIO.HIGH)
            GPIO.output(ev13,GPIO.LOW)
            cycle_data.append(0)
            cycle_data.append(0)
            cycle_data.append(1)
            ev13c+=1
            time.sleep(0.5)
        if i == 6:
            GPIO.output(ev08,GPIO.HIGH)
            GPIO.output(ev09,GPIO.HIGH)
            GPIO.output(ev13,GPIO.HIGH)
            cycle_data.append(0)
            cycle_data.append(0)
            cycle_data.append(0)
            time.sleep(0.5)
        dataBase.addCycleData(cycle_data)
    except:
        pass
    finally:
        GPIO.output(ev08,GPIO.HIGH)
        GPIO.output(ev09,GPIO.HIGH)
        GPIO.output(ev13,GPIO.HIGH)
    return cycle_data,ev08c,ev09c,ev13c