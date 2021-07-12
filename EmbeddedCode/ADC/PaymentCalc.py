#Payment Calculator using Raspberry PI and MCP3008 ADC Chip
#Lillian C. Gwendolyn 07/11/2021 @ Wonderfil

#init code taken from https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#mcp.read_adc(i) where i is the port from 0 to 7

#reimann sum thoughts:
#how big of an array of values?
#0-1024 is our values which is 2^10 so 16 bit arrays
#how often to sample?