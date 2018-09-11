#A calculator for calculating two seperate areas of rectangles
#September 11th 2018
#CTI-110 P3T1 - Areas of Rectangles
#James Grimes
#

length1 = float(input("What is the length of the first rectangle?:"))
width1 = float(input("What is the width of the first rectangle?:" ))
area1 = float(length1 * width1)
length2 = float(input("What is the length of the second rectangle?:"))
width2 = float(input("What is the width of the second rectangle?:"))
area2 = float(length2 * width2)

if area1 > area2:
    print('Rectangle 1 has the greater area')
else:
    if area2 > area1:
        print('Rectangle 2 has the greater area') 
    else:
        print('Both are the same area')

input("Press enter to close the program")
