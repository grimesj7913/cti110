#A budget analysis calculator so that you dont go over the budget
# October 4 2018
# CTI-110 P4HW1 - Budget Analysis
# James Grimes
#
total = 0
budget = float(input("How much money are you going to budget : "))
amount = int(input("How many bills do you have to pay : "))

for amount in range (amount):
    print ("How much is bill number", amount + 1, end=': ')
    expenses = float(input())
    total = budget - expenses



if total < 0:
    print ("You are overbudget by $", format(total, '.2f'))
elif total > 0:
    print ("You are still underbudget by $", format(total, '.2f'))
elif total == 0:
    print ("You broke even on your budget!")

input("Press enter to close program")
