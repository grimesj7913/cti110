# Kilometer converter
# October 25th 2018
# CTI-110 P5T1_KilometerConverter 
# James Grimes
#

CONVERSION_FACTOR = 0.6214

def main():

    kilometers = float(input("Enter the distance in kilometers: "))
    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR

    print (km, "kilometers equals", round(miles, 3), "miles")

main()
