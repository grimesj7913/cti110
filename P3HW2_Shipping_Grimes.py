#CTI-110-0001
#P3HW2 - Shipping Charges
#James Grimes
#September 27th 2018
#

pounds = int(input("How much does your package weigh in pounds :"))

if pounds <= 2:
    rate = 1.50
elif pounds <= 6 :
    rate = 3.00
elif pounds <= 10:
    rate = 4.00
elif pounds > 10:
    rate = 4.75

shippingcost = float(rate * pounds)

print ("The total cost of shipping this package is : $", format(shippingcost, '.2f'))

input ("Press enter to close the program")
                     
