# Main file
# currently being used for testing purposes
#
# PDP group 25

from testclass import aux
import RPi.GPIO as GPIO
import time

def say_hello():
    print("Hello World")
    print("It Worked!")

if __name__ == '__main__':
    say_hello()
    aux1 = aux(1,2,3)
    aux1.modify_all()
    aux1.print_all()

    p1 = 32 #high then low
    p2 = 40 #pwm
    p_in = 37 #analog in

#chan_list = [11,12]
# add as many channels as you want!
# you can tuples instead i.e.:
#   chan_list = (11,12)
#GPIO.setup(chan_list, GPIO.OUT)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup((p1,p2),GPIO.OUT)
    GPIO.setup(p_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pwm1 = GPIO.PWM(p2, 1000)
    pwm1.start(50)
    print("pwm started")
    GPIO.output(p1,GPIO.HIGH)
    print("Pin on")
    time.sleep(10)
    GPIO.output(p1,GPIO.LOW)
    print("Pin off")
    time.sleep(2)
    print("begin analog input")
    time.sleep(2)
    for i in range(100000):
        temp = GPIO.input(p_in)
        print (str(temp))
        time.sleep(0.01)
    print("analog input done")


    GPIO.cleanup()

    # this is a test upload


