##############################################
#
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
#   FUTURE - 12v Relay Control for fans
#   FUTURE - External temp #1 (my use for internal media centre)
#   FUTURE - External temp #2 (my use for family room temp)
#   FUTURE - IR Emiiter (my use for family room reverse cycle)
# test edit
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
import pifan_fan as fans
# import pifan_IR
import pifan_tmp as temp

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
FAN1_PULSE = 1       #NUM Pulses from fan per rev 
FAN1_TACHO = 18 
FAN1_LED = 3 
FAN1_PWM = 15 
FAN1_Hz = 20 
FAN1_TYPE="4PIN"
FAN1_NAME="EZDIY-FAB-1"
FAN1_RELAY = 23
####################################################################
FAN3_PULSE = 1       #NUM Pulses from fan per rev 
FAN3_TACHO = 17 
FAN3_LED = 3 
FAN3_PWM = 7 
FAN3_Hz = 20 
FAN3_TYPE="4PIN"
FAN3_NAME="EZDIY-FAB-3"
FAN3_RELAY = 27
####################################################################
try:
    print("Welcome to PiFan")
    fan1 = fans.fan(FAN1_NAME,FAN1_TYPE,FAN1_LED,FAN1_TACHO,FAN1_PWM,FAN1_Hz,FAN1_PULSE,FAN1_RELAY)
    fan2 = fans.fan(FAN2_NAME,FAN2_TYPE,FAN2_LED,FAN2_TACHO,FAN2_PWM,FAN2_Hz,FAN2_PULSE,FAN2_RELAY)
    fan3 = fans.fan(FAN3_NAME,FAN3_TYPE,FAN3_LED,FAN3_TACHO,FAN3_PWM,FAN3_Hz,FAN3_PULSE,FAN3_RELAY)
    fan_bank = [fan1,fan2,fan3] 
    while True:
        for x in fan_bank:
            #time.sleep(2)
            print(x.name, x.rpm, x.last_rpm)
            x.my_rpm() 
            if x.rpm == x.last_rpm: print("{} STALLED").format(x.name)
            """else:
                print(x.name, x.rpm)
                #x.control.start(10)
                #print("STOPPING")
                #x.control.start(0)
                #time.sleep(10)
                x.my_rpm()
                print(x.name, x.rpm)
                #time.sleep(2)
                #print("STARTING")
                x.control.start(100)
                #time.sleep(10)
                x.my_rpm()
                print(x.name, x.rpm) """

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this function




