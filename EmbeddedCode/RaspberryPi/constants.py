#Constants used for payment calc and state machine + inits

#Lillian Cordelia Gwendolyn 07/16/2021 @ Wonderfil

#enum not strictly required but useful for organization
import enum
#used for encoding onto RFID chip
import msgpack

#used for RPI GPIO pins
import RPi.GPIO as GPIO

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#used for RFID reader
from mfrc522 import SimpleMFRC522

RFIDReader = SimpleMFRC522()

#MCP3008 init code taken from https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
#note - software SPI works on any machine with pins plugged in correctly + correct files installed
#but is slightly slower/bulkier than hardware SPI
#hardware SPI requires enabling a few settings on the RP
#but gives slightly better performance

#ports of Raspberry Pi used to drive ADC
#taken from https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
#ports for software-run SPI
ADC_CLK_RP_PIN = 18
ADC_MISO_RP_PIN = 23
ADC_MOSI_RP_PIN = 24
ADC_CS_RP_PIN = 25
#ports for hardware-run SPI
ADC_RP_SPI_PORT = 0
ADC_RP_SPI_DEVICE = 0

# Software SPI configuration:
mcp = Adafruit_MCP3008.MCP3008(clk=ADC_CLK_RP_PIN, cs=ADC_CS_RP_PIN, \
	miso=ADC_MISO_RP_PIN, mosi=ADC_MOSI_RP_PIN)

# Hardware SPI configuration:
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(ADC_RP_SPI_PORT, ADC_RP_SPI_DEVICE))

#timing constants
SAMPLE_INTERVAL = 0.05 #20x/sec
MAX_TIMEOUT = 30 #30 sec max

#LIST_SIZE = (MAX_TIMEOUT / SAMPLE_INTERVAL)

#.5V when converted to ADCs 0-1024 scale = 155
#number is used as the maximum for us to consider the pot to still be off
ADC_MAX_OFF_DIGITAL_VOLTAGE = 155

#states used for WF state machine
class WF_STATE(enum.Enum):
	ERROR = -1
	WAITING_FOR_CUSTOMER = 0
	FOB_SELECTED = 1
	READY_FOR_POUR = 2
	RUNNING = 3
	POUR_COMPLETED = 4
	PROGRAM_FOB = 5
	#SHOW_DATA_ON_TERMINAL = 6

#number of taps we are using
NUM_TAPS = 4

#ports of ADC chip used for each tap
WF_TAP_ONE_ADC_PIN = 0
WF_TAP_TWO_ADC_PIN = 2
WF_TAP_THREE_ADC_PIN = 4
WF_TAP_FOUR_ADC_PIN = 6

#enum to organize by tap numbers so i dont need to use numbers
#doubles as port used for ADC chip reading
#0-7 correspond to pins 0-7 on the chip

class WF_TAP(enum.Enum):
	NONE = -1
	ONE = WF_TAP_ONE_ADC_PIN
	TWO = WF_TAP_TWO_ADC_PIN
	THREE = WF_TAP_THREE_ADC_PIN
	FOUR = WF_TAP_FOUR_ADC_PIN

#object for what a tap needs to store
class WF_TAP_DATA:
	TapNum = WF_TAP.NONE
	ProductName = "Placeholder"
	CostPerML = 0.00

	def __init__(self, tapnum, productname, costperml) -> None:
		self.TapNum = tapnum
		self.ProductName = productname
		self.CostPerML = costperml

	def EncodeTapData(self, volOut):
		return msgpack.packb({ 
			"Tap": self.TapNum,
			"ProductName": self.ProductName,
			"TotalVolOutput": volOut,
			"TotalCost": volOut * self.CostPerML
		})
	
	#decode is used for setting the Wonderfil's taps
	#to have new product names and costs
	#it is not to receive the data encoded above
	#as that part is handled by the cashier within the Wonderfil app
	def DecodeTapData(self, packedInfo):
		return msgpack.unpackb(packedInfo)
