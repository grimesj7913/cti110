# A program on the tution increased by percentages
# October 23rd 2018
# CTI-110 P4HW3 - Tuition Increase
# James Grimes
#

tuition = 8000

print()
print("Year\tTuition")
print("-------------")

for years in range (1, 6):
    tuition += ( 0.03 * tuition)
    print(years, '\t$', format(tuition, ".2f"), sep ="")

input ("Press enter to close the program")
