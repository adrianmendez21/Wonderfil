#Handles the state machine of the Raspberry Pi
#A repository for the functions and data involved
#Essentially a black box for organization

#Lillian Cordelia Gwendolyn 07/14/2021 @ Wonderfil

#time used for delaying current thread to create sampling interval
from time import sleep
#sys used for exiting and throwing errors
from sys import exit

import EmbeddedCode.RaspberryPi.constants as constants

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
	#signal is from fob or verifone
	#meanwhile we check if we recieve a signal on them
   	sleep(1)
   	return

def RunState_FOB_SELECTED():
	global currTap
	global timeRunning
	global totalVolOutput
	global currState
	

	#init things
	timeRunning = 0
	totalVolOutput = 0
	currTap = constants.WF_TAP.NONE
	currState = constants.WF_STATE.READY_FOR_POUR
	return

'''
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
'''

def RunState_READY_FOR_POUR():
	#global currReading
	global timeRunning
	global currState
	global currTap
	#look for first point when adc gets a signal
	for tap in constants.WF_TAP:
		if(tap == constants.WF_TAP.NONE): continue

		currReading = constants.mcp.read_adc(tap)
		if(currReading > constants.ADC_MAX_OFF_DIGITAL_VOLTAGE):
			#must assign in for loop to keep same value of tap
			#otherwise falls out of scope if moved outside loop
			currTap = tap
			break
		else: continue
	
	sleep(constants.SAMPLE_INTERVAL)

	if(currTap == constants.WF_TAP.NONE): return

	#else do math to add reading to total vol output
	#
	#
	timeRunning += constants.SAMPLE_INTERVAL
	currState = constants.WF_STATE.RUNNING
	return

def RunState_RUNNING():
	#global currReading
	global timeRunning
	global currState
	currReading = constants.mcp.read_adc(currTap)
	if((currReading <= constants.ADC_MAX_OFF_DIGITAL_VOLTAGE) or (timeRunning >= constants.constants.MAX_TIMEOUT)):
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
	#send whatever info to fob/verifone
	#prompt user to wrap fob around bottle
	#check for errors
	#global timeRunning
	global currState
	currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
	return

#python doesnt have built in switch case statements
#so instead its a dictionary of functions?
RP_SM = {
	constants.WF_STATE.ERROR: RunState_ERROR,
	constants.WF_STATE.WAITING_FOR_CUSTOMER: RunState_WAITING_FOR_CUSTOMER,
	constants.WF_STATE.TAP_SELECTED: RunState_TAP_SELECTED,
	constants.WF_STATE.READY_FOR_POUR: RunState_READY_FOR_POUR,
	constants.WF_STATE.RUNNING: RunState_RUNNING,
	constants.WF_STATE.POUR_COMPLETED: RunState_POUR_COMPLETED
}
