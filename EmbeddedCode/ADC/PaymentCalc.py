#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Lillian Cordelia Gwendolyn 07/13/2021 @ Wonderfil

import EmbeddedCode.ADC.constants as constants

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#time used for delaying current thread to create sampling interval
import time
#sys used for exiting and throwing errors
import sys

#MCP3008 init code taken from https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
#note - software SPI works on any machine with pins plugged in correctly + correct files installed
#but is slightly slower/bulkier than hardware SPI
#hardware SPI requires enabling a few settings on the RP
#but gives slightly better performance

# Software SPI configuration:
mcp = Adafruit_MCP3008.MCP3008(clk=constants.ADC_CLK_RP_PIN, cs=constants.ADC_CS_RP_PIN, miso=constants.ADC_MISO_RP_PIN, mosi=constants.ADC_MOSI_RP_PIN)

# Hardware SPI configuration:
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(constants.ADC_RP_SPI_PORT, constants.ADC_RP_SPI_DEVICE))

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
   time.sleep(5)
   return

def RunState_WAITING_FOR_CUSTOMER():
   #if signal currState = constants.WF_STATE.TAP_SELECTED
   time.sleep(1)
   return

def RunState_TAP_SELECTED():
   #get tap from exterior signal
   currTap = constants.WF_TAP.ONE
   #init things
   timeRunning = 0
   totalVolOutput = 0
   currState = constants.WF_STATE.READY_FOR_POUR
   return

def RunState_READY_FOR_POUR():
   #look for first point when adc gets a signal
   currReading = mcp.read_adc(currTap)
   if(currReading == 0):
      #wait one interval and repeat the check
      time.sleep(constants.SAMPLE_INTERVAL)
      return
   #else do math to add reading to total vol output
   #
   #
   time.sleep(constants.SAMPLE_INTERVAL)
   timeRunning += constants.SAMPLE_INTERVAL
   currState = constants.WF_STATE.RUNNING
   return

def RunState_RUNNING():
   currReading = mcp.read_adc(currTap)
   if((currReading == 0) or (timeRunning >= constants.constants.MAX_TIMEOUT)):
      currState = constants.WF_STATE.POUR_COMPLETED
      return
   #else do math to add reading to total vol output
   #
   #
   time.sleep(constants.SAMPLE_INTERVAL)
   timeRunning += constants.SAMPLE_INTERVAL
   return

def RunState_POUR_COMPLETED():
   #send info to exterior program
   #check for errors
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
   
   time.sleep(constants.SAMPLE_INTERVAL)

#will never be reached, here for propriety
#empty means exit success / return 0
sys.exit()
