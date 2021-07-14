#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Handles the state machine of the RP and communicates with other devices
#To send calculated info to, as well as manage the motors

#Lillian Cordelia Gwendolyn 07/14/2021 @ Wonderfil

#time used for delaying current thread to create sampling interval
from time import sleep
#sys used for exiting and throwing errors
from sys import exit

import EmbeddedCode.RaspberryPi.constants as constants
import EmbeddedCode.RaspberryPi.statemachine as SM

#background -
#there is only one terminal, and only one tap can run at any given time
#so essentially there is a reset between every user
#thus we are essentially doing a one-hot version of the taps
#instead of treating them as separate instances

#TODO:
#get formula so that do not need to keep track of every value taken
#and instead constantly add to formula so that receiving devices
#always get the current amnt of volume exported

#remove excess ticks from either main loop or from state machine

#go back through imports and only take what is needed - dont need to store excess imports

#task loop
#runs state machine every tick
while True:
	SM.RP_SM[SM.currState]()

	sleep(constants.SAMPLE_INTERVAL)

#will never be reached, here for propriety
#empty means exit success / return 0
sys.exit()
