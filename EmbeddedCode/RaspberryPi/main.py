#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Handles the state machine of the RP and communicates with other devices
#To send calculated info to, as well as manage the motors

#Lillian Cordelia Gwendolyn 07/15/2021 @ Wonderfil

#time used for delaying current thread to create sampling interval
from time import sleep
#sys used for exiting and throwing errors
from sys import exit

#used for RPI GPIO pins
import RPi.GPIO as GPIO

import EmbeddedCode.RaspberryPi.constants as constants
import EmbeddedCode.RaspberryPi.statemachine as SM

#background -
#there is only one terminal, and only one tap can run at any given time
#so essentially there is a reset between every user
#thus we are essentially doing a one-hot version of the taps
#instead of treating them as separate instances

#TODO:
#terminal integration

#consider removing initial fob requirement - only use fob at end
#to handle final payment, and instead wait until someone pours from tap
#to start?

#main block
#try except finally from https://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
try:
	#task loop
	#runs state machine every tick
	while True:
		SM.RP_SM[SM.currState]()

		sleep(constants.SAMPLE_INTERVAL)

except KeyboardInterrupt:
	print("exited by ctrl c keyboard interrupt exception")

except:
	print("exited by non keyboard exception")

finally:
	#will never be reached unless exception occurs, here for propriety
	#resets used gpio pins
	GPIO.cleanup()
	#empty means exit success / return 0
	exit()
