##############################################
# MrCoolPi - 
# PiFan - PWM fan xomtroller for RasPi
# 
# mrfatbat Jul 2021
# mrfatbat@gmail.com
# v0.0.1 210724
# v0.0.2 210726 -- Some sort of fan stuff.... fan module getting there.
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
import mrcoolpi_shift as shift
#import mrcoolpi_relay as relay
#import mrcoolpi_cli as cli
#import mrcoolpi_led as led
#import mrcoolpi_zone as zone


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



    # RELAY / SERIAL SHIFT TEST
    tst_shift = shift.shift(9,22,10)

    tst_shift.set([1,0,0,0,0,0,0,0])
    time.sleep(1)
    tst_shift.set([0,1,0,0,0,0,0,0])
    time.sleep(1)
    tst_shift.set([0,0,1,0,0,0,0,0])
    time.sleep(1)
    tst_shift.set([0,0,0,1,0,0,0,0])
    time.sleep(1)
    tst_shift.set([0,0,0,0,1,0,0,0])
    time.sleep(1)
    tst_shift.set([0,0,0,0,0,1,0,0])
    time.sleep(1)
    tst_shift.set([0,0,0,0,0,0,1,0])
    time.sleep(1)
    tst_shift.set([0,0,0,0,0,0,0,1])
    time.sleep(1)

    tst_shift.set([1,1,1,1,1,1,1,1])
    time.sleep(5)
    tst_shift.set([0,0,0,0,0,0,0,0])


except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this function




