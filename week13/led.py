import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12
LED = 11

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(LED, 100)
p.start(0)

time.sleep(0.1)

while True:
    # Dept
    GPIO.output(TRIG, 1)
    time.sleep(0.001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    dept = (stop - start) * 17000
    print(dept)
    print('-'*20)

    # LED
    try:
        p.ChangeDutyCycle(100 - dept * 5)
    except:
        pass

    time.sleep(0.2)
p.stop()
GPIO.cleanup()