# PiFan -pifan_fan - fan controller
# Does not pickup rpms dropping to zero!  will pickup start at zero.....

import RPi.GPIO as GPIO
import time
import copy

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup variables
#t = time.time()
#tmp_rpm = 0
min_rpm = 300
FAN_POLL_WAIT_TIME = 1  # [s] Time to wait between each refresh

# Caculate pulse frequency and RPM
def fell(n):
    global t
    global tmp_rpm
    #t = time.time()
    dt = time.time() - t
    if dt < 0.005: 
        return # Reject spuriously short pulses
    freq = 1 / dt
    tmp_rpm = (freq / tmp_pulse) * 60
    #print("{} TMP_RPM FELL").format(tmp_rpm)
    t = time.time()

def led_on(fan):
    #print("COOLING")
    GPIO.output(fan.led, True)

def led_off (fan):
    #print("NOT COOLING")
    GPIO.output(fan.led, False)


class fan:
    
    def fell2(self):
        global t
        global tmp_rpm
        #t = time.time()
        dt = time.time() - t
        if dt < 0.005: 
            return # Reject spuriously short pulses
        freq = 1 / dt
        tmp_rpm = (freq / tmp_pulse) * 60
        print("{} TMP_RPM FELL").format(tmp_rpm)
        t = time.time()

    def my_rpm(self):
        global t 
        global tmp_rpm
        GPIO.add_event_detect(self.tacho, GPIO.FALLING, fell)
        self.last_rpm = copy.copy(self.rpm)
        time.sleep(FAN_POLL_WAIT_TIME)
        self.rpm = tmp_rpm
        if tmp_rpm < min_rpm:
            led_off(self)
        else:
            led_on(self)    
        GPIO.remove_event_detect(self.tacho)
        return(self.rpm)
        
    def pwr_on(self):
        GPIO.output(self.relay,GPIO.HIGH) # FAN ON!  RELAY

    def pwr_off(self):
        GPIO.output(self.relay,GPIO.LOW) # FAN ON!  RELAY

    def __init__(self,name,fan_type,led,tacho,pwm,hz,pulse,relay):
	      global tmp_rpm 
        global t
        global tmp_pulse
        t = time.time()
        self.name = name
	      self.type = fan_type
	      self.led = led
	      self.pulse = pulse
	      self.tacho = tacho
        self.relay = relay
        self.last_rpm = 0
        tmp_rpm = 0
        tmp_pulse = pulse
	      GPIO.setup(led,GPIO.OUT) # FAN1_LED
        GPIO.setup(relay,GPIO.OUT)
        GPIO.output(relay,GPIO.LOW) # FAN OFF WHEN INIT
	GPIO.setup(tacho, GPIO.IN, pull_up_down=GPIO.PUD_UP) # FAN1_TACHO PUP 3.3V
        #GPIO.add_event_detect(tacho, GPIO.FALLING, fell)
	self.rpm = tmp_rpm
        #print("{} RPM IN INIT").format(self.rpm)
        self.pwm = pwm
        self.hz = hz
        if fan_type == "4PIN":
            GPIO.setup(pwm, GPIO.OUT, initial=GPIO.LOW)
            self.control = GPIO.PWM(pwm,hz)
        print("FAN {} CREATED").format(self.name)
    




