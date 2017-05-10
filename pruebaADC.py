import time
import Adafruit_ADS1x15 as ADC1115

adc = ADC1115.ADS1115()		##Se crea el ADC de 16 bits
#adc = ADC1115.ADS1015(address=0x49, busnum=1)  ##Se puede cambiar la direccion del ADC I2C

# Ganancias:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V

GAIN = 2

adc.start_adc(0, gain=GAIN) ##Canal 0 con ganancia 2


print('Reading ADS1x15 channel 0 for 5 seconds...')
start = time.time()
while (time.time() - start) <= 5.0:
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!
    print('Channel 0: {0}'.format(value))
    # Sleep for half a second.
    time.sleep(0.5)

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc.stop_adc()
