#CTI-110-0001
#P3HW1 - Roman Numerals
#James Grimes
#September 27th 2018
#

number = int(input("Enter a number 1 - 10:"))

if (number > 10):
    print("ERROR : The number is above the range of 10!")
elif (number <= 0):
    print("ERROR : The number is below the range of 1")
elif (number == 1):
    print("The roman numeral for the number one is : I")
elif (number == 2):
    print("The roman numeral for the number two is : II")
elif (number == 3):
    print("The roman numeral for the number three is : III")
elif (number == 4):
    print("The roman numeral for the number four is : IV")
elif (number == 5):
    print("The roman numeral for the number five is : V")
elif (number == 6):
    print("The roman numeral for the number six is : VI")
elif (number == 7):
    print("The roman numeral for the number seven is : VII")
elif (number == 8):
    print("The roman numeral for the number eight is : VIII")
elif (number == 9):
    print("The roman numeral for the number nine is : IX")
elif (number == 10):
    print("The roman numeral for the number ten is : X")

input("Press enter to exit program")
