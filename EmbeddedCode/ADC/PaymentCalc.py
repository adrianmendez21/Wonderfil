#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Lillian Cordelia Gwendolyn 07/13/2021 @ Wonderfil

import EmbeddedCode.ADC.constants as constants

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#time used for delaying current thread to create sampling interval
import time
#sys used for exiting and throwing errors
import sys

#init code taken from https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
# Software SPI configuration:
mcp = Adafruit_MCP3008.MCP3008(clk=constants.ADC_CLK_RP_PIN, cs=constants.ADC_CS_RP_PIN, miso=constants.ADC_MISO_RP_PIN, mosi=constants.ADC_MOSI_RP_PIN)

# Hardware SPI configuration:
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(constants.ADC_RP_SPI_PORT, constants.ADC_RP_SPI_DEVICE))

#

#TODO:
#get formula so that do not need to keep track of every value taken
#and instead constantly add to formula so that receiving devices
#always get the current amnt of volume exported

#boolean to see if we use them, right now we only use one tap
#will eventually be managed by an exterior thread instead of handled manually
CurrentTap = 0
WF_TAP_ONE_ON = True
WF_TAP_TWO_ON = False
WF_TAP_THREE_ON = False
WF_TAP_FOUR_ON = False

#create 4 empty lists to store speeds taken over pouring
WF_TAP_ONE_Speed_List = 0 * constants.LIST_SIZE
WF_TAP_TWO_Speed_List = 0 * constants.LIST_SIZE
WF_TAP_THREE_Speed_List = 0 * constants.LIST_SIZE
WF_TAP_FOUR_Speed_List = 0 * constants.LIST_SIZE

#individual indeces for each speed list
WF_TAP_ONE_List_Index = 0
WF_TAP_TWO_List_Index = 0
WF_TAP_THREE_List_Index = 0
WF_TAP_FOUR_List_Index = 0

#task loop
while True:

    if(constants.WF_TAP_ONE_ON and (WF_TAP_ONE_List_Index < constants.LIST_SIZE)):

       WF_TAP_ONE_Speed_List[WF_TAP_ONE_List_Index] = mcp.read_adc(constants.WF_TAP_ONE_ADC_PIN)
       ++WF_TAP_ONE_List_Index

    if(constants.WF_TAP_TWO_ON and (WF_TAP_TWO_List_Index < constants.LIST_SIZE)):
        
       WF_TAP_TWO_Speed_List[WF_TAP_TWO_List_Index] = mcp.read_adc(constants.WF_TAP_TWO_ADC_PIN)
       ++WF_TAP_TWO_List_Index

    if(constants.WF_TAP_THREE_ON and (WF_TAP_THREE_List_Index < constants.LIST_SIZE)):
        
       WF_TAP_THREE_Speed_List[WF_TAP_THREE_List_Index] = mcp.read_adc(constants.WF_TAP_THREE_ADC_PIN)
       ++WF_TAP_THREE_List_Index

    if(constants.WF_TAP_FOUR_ON and (WF_TAP_FOUR_List_Index < constants.LIST_SIZE)):
        
       WF_TAP_FOUR_Speed_List[WF_TAP_FOUR_List_Index] = mcp.read_adc(constants.WF_TAP_FOUR_ADC_PIN)
       ++WF_TAP_FOUR_List_Index

    #send all info to payment terminal every few cycles - needs math of everything + curr duration of tap
    
    time.sleep(constants.SAMPLE_INTERVAL)

#will never be reached, here for propriety
#empty means exit success / return 0
sys.exit()
