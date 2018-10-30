# A conversion program from one foot (measurement) to inches
#October 30th 2018
# CTI-110 P5T2_FeetToInches 
# James Grimes
#
inches_per_foot = 12
def main():
    feet = int(input("How long is the object in feet? : "))
    print (feet, 'equals', feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * inches_per_foot

main()

input("Press enter to close program")
