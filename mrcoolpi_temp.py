import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

#GPIO for Status LEDS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

	
def raspi_cpu_temp():
	print("Obtaining RasPi CPU Temp....")
	cpu = CPUTemperature()
	print(cpu.temperature)
	
def __init__(self,tmp_snsr_name,tmp_snsr_type,tmp_snsr_io):
  self.name = tmp_snsr_name
  self.type = tmp_snsr_type
  self.io = tmp_snsr_io
  self.tmp = 0
  self.last_tmp = 0
  self.avg_tmp = 0
  if self.type == "RPiCPU": pass
  
  
  
  


