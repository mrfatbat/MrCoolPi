import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

#GPIO for Status LEDS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT) #HEAT LED

# HEAT MONITORING ##
def led_tmp_hi_on():
	print("TEMP HIGH")
	GPIO.output(11, True)
	
def sen_tmp_raspi_cpu():
	print("Obtaining RasPi CPU Temp....")
	cpu = CPUTemperature()
	print(cpu.temperature)


def led_tmp_hi_off():
	GPIO.output(11, False)

###################