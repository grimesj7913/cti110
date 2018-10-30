# A program that can tell users if its a prime number or not
# October 30th 2018
# CTI-110 P5HW1 - Prime Numbers
# James Grimes
#
#              PSEUDOCODE BELOW
# user is prompted to input a number
# the number goes through the programming calcuation to see if its a prime number
# if the input is less than one then it is a prime number
# if the input is greater than two then it goes to next step
# the next step is that it goes through this formula (2, number//2+1)
# if the end value equals to 0 then it is not a prime number
# if the end value doesnt equal to 0 then it is a prime number
# program completes the calculations
# if the is_prime function returns true then user gets the is_prime message
# if the is_prime function returns false then user gets a print message
# end program



def is_prime(number):
    if (number<2):
        return False
    for i in range (2, number//2+1):
        if (number%i==0):
            return False
        return True
number=int(input("Enter a number to see if its a prime number : "))
if is_prime(number):
    print(number,"is a prime number!")
else: print(number,"is not a prime number!")

input("Press enter to close program")
    
