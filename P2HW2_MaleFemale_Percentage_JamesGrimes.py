# A male/female percentage program/calculator
# September 4th 2018
# CTI-110 P2HW2 - Male Female Percentage
# James Grimes
#


males = float(input("How many male students are in the class? : "))
females = float(input("How many females students are in the class? : "))
classtotal = float(males + females)
malepercentage = float(males / classtotal)
femalepercentage = float(females / classtotal)

print ("The male percentage is", malepercentage, "%")
print ("The female percentage is", femalepercentage, "%")

input ("Press enter to close the program.")
