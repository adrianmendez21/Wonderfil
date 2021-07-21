#Handles the state machine of the Raspberry Pi
#A repository for the functions and data involved
#Essentially a black box for organization

#Lillian Cordelia Gwendolyn 07/21/2021 @ Wonderfil

#time used for delaying current thread to create sampling interval
from time import sleep, time
#sys used for exiting and throwing errors
from sys import exit

import constants as constants

#eventually replace with placeholder info
tap = [constants.WF_TAP_DATA(constants.WF_TAP.NONE, -1,"placeholder", 0.00), \
	constants.WF_TAP_DATA(constants.WF_TAP.ONE, constants.ADC_CH0, "Pantene Conditioner", 0.06), \
	constants.WF_TAP_DATA(constants.WF_TAP.TWO, constants.ADC_CH1, "Tresemme Shampoo", 0.03), \
	constants.WF_TAP_DATA(constants.WF_TAP.THREE, constants.ADC_CH2, "Sauve Essentials Body Wash", 0.10), \
	constants.WF_TAP_DATA(constants.WF_TAP.FOUR, constants.ADC_CH3, "Head And Shoulders 2 in 1", 0.05)]

#enums for state
currTap = 0
currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
#time spent running current tap - used to track if timeout should occur
timeRunning = 0
#last time reading so we know how much time has passed
prevTimeAccessed = 0
#tracking how much volume has been exported over this pour
totalVolOutput = 0

#ID of current fob being used
fob_ID = 0

def RunState_ERROR():
   	print("Wonderfil has encountered an error\n")
   	sleep(5)
   	return

def RunState_WAITING_FOR_CUSTOMER():
	global fob_ID
	global currState
   	#if signal currState = constants.WF_STATE.TAP_SELECTED
	#signal is from fob or verifone
	#meanwhile we check if we recieve a signal on them

	print("idle - scan fob")

	#ASSUMEDLY this should wait for a card to come by then
	#store the ID and reset it
	try:
		#fob_ID = constants.RFIDReader.read_id()

		#if we read in that it has been prewritten to program wonderfil
		#then skip blanking it and enter separate programming state

		#need to better plan what we encode
		#reset text on reader hopefully
		#need to also upgrade to the non-simplified version
		#so that we can specify the exact data to read and write
		#constants.RFIDReader.write("")
		print("this is where reading and writing would happen on the fob")
	
	except:
		print("fob error")
		return

	#if has not returned then assumedly has found and reset a fob
	currState = constants.WF_STATE.FOB_SELECTED

	return

def RunState_FOB_SELECTED():
	global currTap
	global timeRunning
	global prevTimeAccessed
	global totalVolOutput
	global currState

	print("fob selected - initializing")

	#init things
	timeRunning = 0
	prevTimeAccessed = time()
	totalVolOutput = 0
	currTap = 0
	currState = constants.WF_STATE.READY_FOR_POUR
	return

def RunState_READY_FOR_POUR():
	#global totalVolOutput
	global timeRunning
	global prevTimeAccessed
	global currState
	global currTap
	#look for first point when adc gets a signal
	#read through all 4 taps' adc values

	print("ready to pour - select tap")

	for i in range(1, constants.NUM_TAPS + 1):

		print("inside range block")

		print("reading tap ", i)
		currReading = tap[i].ADC_Ch.voltage
		print("val = ", currReading)
		if(currReading > constants.ADC_MAX_OFF_VOLTAGE):
			#must assign in for loop to keep same value of tap
			#otherwise falls out of scope if moved outside loop
			print("have selected tap", i)
			currTap = i
			break
		else: continue

	#if has not selected tap OR error in range/tap assignment
	if(currTap == 0): return

	#else do math to add reading to total vol output
	#
	#

	print("tap ", currTap.tapNum, " has been selected")

	currTime = time()
	timeRunning += currTime - prevTimeAccessed
	prevTimeAccessed = currTime
	#timeRunning += constants.SAMPLE_INTERVAL
	currState = constants.WF_STATE.RUNNING
	return

def RunState_RUNNING():
	#global totalVolOutput
	global timeRunning
	global prevTimeAccessed
	global currState

	print("running - release tap to stop")

	currReading = tap[currTap].ADC_Ch.voltage
	if((currReading <= constants.ADC_MAX_OFF_DIGITAL_VOLTAGE) \
		 or (timeRunning >= constants.MAX_TIMEOUT)):
		currState = constants.WF_STATE.POUR_COMPLETED
		return

	print(currReading)

	#else do math to add reading to total vol output
	#
	#
	currTime = time()
	timeRunning += currTime - prevTimeAccessed
	prevTimeAccessed = currTime
	#timeRunning += constants.SAMPLE_INTERVAL
	return

def RunState_POUR_COMPLETED():
	#send info to exterior program
	#send whatever info to fob/verifone
	#prompt user to wrap fob around bottle
	#check for errors
	#global timeRunning
	global currState

	print("pour complete - calculating cost")
	
	#sum costs
	totalCost = totalVolOutput
		
	currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
	return

def RunState_PROGRAM_FOB():
	global currState
	global fob_ID

	print("pour complete - writing to fob")

	#goal is to program info on fob so clerk can check out
	#by producing barcode from RFID data to then scan and use

	try:
		#if(fob_ID == constants.RFIDReader.read_id()):
			#update write to include better management of where things go
			#eg block 1 name block 2 price block 3 data
			#encodes using msgpack
			#constants.RFIDReader.write(currTap.EncodeTapData(totalVolOutput))
			#print("id read" + fob_ID)
			print("this is where reading and writing would happen on the fob")
		#else:
			#return
	
	except:
		print("fob error")
		return

	#display sale on terminal for x seconds then back to idle state
	sleep(5)
	currState = constants.WF_STATE.WAITING_FOR_CUSTOMER
	return

#python doesnt have built in switch case statements
#so instead its a dictionary of functions?
RP_SM = {
	constants.WF_STATE.ERROR: RunState_ERROR,
	constants.WF_STATE.WAITING_FOR_CUSTOMER: RunState_WAITING_FOR_CUSTOMER,
	constants.WF_STATE.FOB_SELECTED: RunState_FOB_SELECTED,
	constants.WF_STATE.READY_FOR_POUR: RunState_READY_FOR_POUR,
	constants.WF_STATE.RUNNING: RunState_RUNNING,
	constants.WF_STATE.POUR_COMPLETED: RunState_POUR_COMPLETED,
	constants.WF_STATE.PROGRAM_FOB: RunState_PROGRAM_FOB
}
