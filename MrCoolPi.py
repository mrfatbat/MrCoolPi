##############################################
# MrCoolPi - 
# PiFan - PWM fan xomtroller for RasPi
# 
# mrfatbat Jul 2021
# mrfatbat@gmail.com
# v0.0.1 210724
# v0.0.2 210126 -- Some sort of fan stuff.... fan module getting there.
#
# DEV ROADMAP FOR FUNCTUONALITY
#   BETA - Read tacho - getting weird values. works fine when PWM speed is set to zero, gives weird shit
#         when it gets any speed setting over zero
#   WIP - Get CPU Temp
#   FUTURE - Web Page / API
#   WIP - Utilise PWM
#   WIP 12v Relay Control for fans - direct through Pi but need to kove over to shifter
#   FUTURE - External temp #1 (my use for internal media centre)
#   FUTURE - External temp #2 (my use for family room temp)
#   FUTURE - IR Emiiter (my use for family room reverse cycle)
# 
#
# DEV ROADMAP FOR CODE
#   WIP - Split into seperate files
#   WIP - Arrays and objects
#
###############################################

#Headers
import RPi.GPIO as GPIO
import time
import copy
# import pifan_web as web
# import pifan_pwm
import mrcoolpi_fan as fans
# import pifan_IR
import mrcoolpi_temp as temp
import mrcoolpi_io as io
import mrcoolpi_relay as relay
import mrcoolpi_cli as cli


# Some inital comtrol/debug variables
mrcoolpi_status = "PROTO"


# Initialise all the classes

# Initalise the MCP's 

# Initialise the Serial Shifter

####################################################################
FAN1_PULSE = 1       #NUM Pulses from fan per rev 
FAN1_TACHO = 25 
FAN1_LED = 3 
FAN1_PWM = 15 
FAN1_Hz = 20 
FAN1_TYPE="4PIN"
FAN1_NAME="EZDIY-FAB-1"
FAN1_RELAY = 23
#############################################################
FAN2_PULSE = 1       #NUM Pulses from fan per rev 
FAN2_TACHO = 2 
FAN2_LED = 3 
FAN2_PWM = 4 
FAN2_Hz = 20 
FAN2_TYPE="4PIN"
FAN2_NAME="EZDIY-FAB-2"
FAN2_RELAY= 24
####################################################################
FAN3_PULSE = 1       #NUM Pulses from fan per rev 
FAN3_TACHO = 18 
FAN3_LED = 3 
FAN3_PWM = 7 
FAN3_Hz = 20 
FAN3_TYPE="4PIN"
FAN3_NAME="EZDIY-FAB-3"
FAN3_RELAY = 27
####################################################################
try:
    print("Welcome to Mr Cool Pi!")

    #create fan objects - fans off at relay on init
    fan1 = fans.fan(FAN1_NAME,FAN1_TYPE,FAN1_LED,FAN1_TACHO,FAN1_PWM,FAN1_Hz,FAN1_PULSE,FAN1_RELAY)
    fan2 = fans.fan(FAN2_NAME,FAN2_TYPE,FAN2_LED,FAN2_TACHO,FAN2_PWM,FAN2_Hz,FAN2_PULSE,FAN2_RELAY)
    fan3 = fans.fan(FAN3_NAME,FAN3_TYPE,FAN3_LED,FAN3_TACHO,FAN3_PWM,FAN3_Hz,FAN3_PULSE,FAN3_RELAY)
    
    #create a list of all the fans
    fan_bank = [fan1,fan2,fan3] 
    
    #TESTING During Protype



   while True:
        for fan in fan_bank:
            print(fan.name, fan.rpm, fan.last_rpm)
            time.sleep(1)
            fan.pwr_on()
            fan.my_rpm() 
            if fan.rpm == fan.last_rpm: print("{} STALLED").format(fan.name)
            print(fan.name, fan.rpm, fan.last_rpm)
            
        time.sleep(5)
        
        for fan in fan_bank:
            print(fan.name, fan.rpm, fan.last_rpm)
            if fan.rpm == fan.last_rpm: print("{} STALLED").format(fan.name)

        time.sleep(5)
        for fan in fan_bank:
            print(fan.name, fan.rpm, fan.last_rpm)
            fan.pwr_off()

        time.sleep(5)
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this function




