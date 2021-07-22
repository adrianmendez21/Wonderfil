#Constants used for payment calc and state machine + inits

#Lillian Cordelia Gwendolyn 07/21/2021 @ Wonderfil

#enum not strictly required but useful for organization
import enum
#used for encoding onto RFID chip
#import msgpack

#used for RPI GPIO pins
import RPi.GPIO as GPIO

#libraries needed for MCP3008 - https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx/
#also https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
#note from producer of MCP3008 using circuitpython library:
#Even though the MCP3008 is a 10-bit ADC, the value returned
#is a 16-bit number to provide a consistent interface
#across ADCs in CircuitPython
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#used for RFID reader
from mfrc522 import SimpleMFRC522

RFIDReader = SimpleMFRC522()

#code to init MCP3008 ADC chip
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create output pins
ADC_CH0 = AnalogIn(mcp, MCP.P0)
ADC_CH1 = AnalogIn(mcp, MCP.P1)
ADC_CH2 = AnalogIn(mcp, MCP.P2)
ADC_CH3 = AnalogIn(mcp, MCP.P3)

#ADC can be accessed from doing
#ADC_CH0.value or ADC_CH0.voltage
#value returns 0 to 65472
#voltage returns 0 to VREF (3.3v)

#timing constants
SAMPLE_INTERVAL = 0.50 #20x/sec
MAX_TIMEOUT = 30 #30 sec max

#LIST_SIZE = (MAX_TIMEOUT / SAMPLE_INTERVAL)

#ADC can return voltage value, so we use that
#instead of digital value
ADC_MAX_OFF_VOLTAGE = 1.5

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

#enum to organize by tap numbers so i dont need to use numbers

class WF_TAP(enum.Enum):
	NONE = -1
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4

#object for what a tap needs to store
class WF_TAP_DATA:
	TapNum = WF_TAP.NONE
	ADC_Ch = ADC_CH0
	ProductName = "Placeholder"
	CostPerML = 0.00

	def __init__(self, tapnum, adc_ch, productname, costperml) -> None:
		self.TapNum = tapnum
		self.ADC_CH = adc_ch
		self.ProductName = productname
		self.CostPerML = costperml
		