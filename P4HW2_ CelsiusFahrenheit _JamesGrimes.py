# A program that uses the conversion of celcius to farenheit 
# October 18th 2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# James Grimes
#


print()
print("Celsius\tFarenheit")
print("------------------")

for celsius in range(0, 21):
    farenheit = (9/5 * celsius) + 32
    print(celsius, '\t', farenheit)

input("Press enter to close the program")
