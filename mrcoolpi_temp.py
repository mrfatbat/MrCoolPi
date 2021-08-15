import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

#GPIO for Status LEDS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT) #HEAT LED
	
def raspi_cpu_temp():
	print("Obtaining RasPi CPU Temp....")
	cpu = CPUTemperature()
	print(cpu.temperature)

