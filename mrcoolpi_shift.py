#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Nov 8th, 2020
# Version: 1.0
# Expanded by mrfatbat as a class for shift registers

import RPi.GPIO as GPIO
import copy 

class shift:
    def __init__(self,data,latch,clock):
        self.data = data
        self.latch = latch
        self.clock = clock
        self.command = []
        self.last_command = []

#set pins to putput
        GPIO.setmode(GPIO.BCM)
        GPIO.setup((self.data,self.latch,self.clock),GPIO.OUT)

    def set(self,command):
        self.last_command = copy.deepcopy(self.command)
        self.command = command
  #put latch down to start data sending
        GPIO.output(self.clock,0)
        GPIO.output(self.latch,0)
        GPIO.output(self.clock,1)
  
  #load data in reverse order
        for i in range(7, -1, -1):
            GPIO.output(self.clock,0)
            GPIO.output(self.data, int(self.command[i]))
            GPIO.output(self.clock,1)
  
  #put latch up to store data on register
        GPIO.output(self.clock,0)
        GPIO.output(self.latch,1)
        GPIO.output(self.clock,1)

