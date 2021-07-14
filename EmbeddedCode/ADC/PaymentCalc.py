#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Lillian Cordelia Gwendolyn 07/14/2021 @ Wonderfil

#time used for delaying current thread to create sampling interval
from time import sleep
#sys used for exiting and throwing errors
from sys import exit

import EmbeddedCode.ADC.constants as constants

#background -
#there is only one terminal, and only one tap can run at any given time
#so essentially there is a reset between every user
#thus we are essentially doing a one-hot version of the taps
#instead of treating them as separate instances

#TODO:
#get formula so that do not need to keep track of every value taken
#and instead constantly add to formula so that receiving devices
#always get the current amnt of volume exported

#go back through imports and only take what is needed - dont need to store excess imports

#enums for state
currTap = constants.WF_TAP.ONE
currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
#time spent running current tap - used to track if timeout should occur
timeRunning = 0
#reading from 0 to 1024
currReading = 0
#tracking how much volume has been exported over this pour
totalVolOutput = 0

def RunState_ERROR():
   print("Wonderfil has encountered an error\n")
   sleep(5)
   return

def RunState_WAITING_FOR_CUSTOMER():
   #if signal currState = constants.WF_STATE.TAP_SELECTED
   sleep(1)
   return

def RunState_TAP_SELECTED():
   global currTap
   global timeRunning
   global totalVolOutput
   global currState
   #get tap from exterior signal
   currTap = constants.WF_TAP.ONE
   #init things
   timeRunning = 0
   totalVolOutput = 0
   currState = constants.WF_STATE.READY_FOR_POUR
   return

def RunState_READY_FOR_POUR():
   #global currReading
   global timeRunning
   global currState
   #look for first point when adc gets a signal
   currReading = constants.mcp.read_adc(currTap)
   if(currReading == 0):
      #wait one interval and repeat the check
      sleep(constants.SAMPLE_INTERVAL)
      return
   #else do math to add reading to total vol output
   #
   #
   sleep(constants.SAMPLE_INTERVAL)
   timeRunning += constants.SAMPLE_INTERVAL
   currState = constants.WF_STATE.RUNNING
   return

def RunState_RUNNING():
   #global currReading
   global timeRunning
   global currState
   currReading = constants.mcp.read_adc(currTap)
   if((currReading == 0) or (timeRunning >= constants.constants.MAX_TIMEOUT)):
      currState = constants.WF_STATE.POUR_COMPLETED
      return
   #else do math to add reading to total vol output
   #
   #
   sleep(constants.SAMPLE_INTERVAL)
   timeRunning += constants.SAMPLE_INTERVAL
   return

def RunState_POUR_COMPLETED():
   #send info to exterior program
   #check for errors
   #global timeRunning
   global currState
   currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
   return

#python doesnt have built in switch case statements
#so instead its a dictionary of functions?
ADC_SM = {
   constants.WF_STATE.ERROR: RunState_ERROR,
   constants.WF_STATE.WAITING_FOR_CUSTOMER: RunState_WAITING_FOR_CUSTOMER,
   constants.WF_STATE.TAP_SELECTED: RunState_TAP_SELECTED,
   constants.WF_STATE.READY_FOR_POUR: RunState_READY_FOR_POUR,
   constants.WF_STATE.RUNNING: RunState_RUNNING,
   constants.WF_STATE.POUR_COMPLETED: RunState_POUR_COMPLETED
}


#task loop
while True:

   ADC_SM[currState]()
   
   sleep(constants.SAMPLE_INTERVAL)

#will never be reached, here for propriety
#empty means exit success / return 0
sys.exit()