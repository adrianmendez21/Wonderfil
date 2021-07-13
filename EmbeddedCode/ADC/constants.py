#Constants used for payment calc / equivalent of #defines in c
#Lillian Cordelia Gwendolyn 07/13/2021 @ Wonderfil

#timing constants
SAMPLE_INTERVAL = 0.01 #100x/sec
MAX_TIMEOUT = 30 #30 sec max

LIST_SIZE = (MAX_TIMEOUT / SAMPLE_INTERVAL)

#ports of ADC chip used for each tap
#0-7 correspond to pins 0-7 on the chip
WF_TAP_ONE_ADC_PIN = 0
WF_TAP_TWO_ADC_PIN = 2
WF_TAP_THREE_ADC_PIN = 4
WF_TAP_FOUR_ADC_PIN = 6

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
