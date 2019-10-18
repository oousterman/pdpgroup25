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

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)



