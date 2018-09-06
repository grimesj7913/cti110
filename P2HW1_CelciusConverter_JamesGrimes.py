# A program that converts celcius to farenheit
# August 30th 2018
# CTI-110 P2HW1 - Celcius Farenheit Converer
# James Grimes
#
#Prompts user to enter celcius data for the formula
celcius = float(input('What is the temperature in celcius?: '))

# Basic formula for celcius to farenheit conversion
farenheit = float(9 / 5 * celcius + 32)

#message for the converted degrees
print("The temperature in farenheit is", farenheit)

input ("Press any key to close")
