import math #imports math library

def is_prime(num): # function for is it a prime number check
    if num <= 1: #checks if number is less than or equal to 1
        return False #returns false as a prime can't be less than 1 or 1
    if num <= 3: #checks if number is less tahn or equal to 3
        return True #this accounts for 3 and number 2 as they both are prime.
    if num % 2 == 0 or num % 3 == 0: #if the a number has no remainder when divided by 2 or 3 return false.
        return False # a prime is a number that can only be divided by itself so this returns false when a number is divisable by 2 or 3. 2 and 3 were already printed in previous lines so no need to worry about them here.
    i = 5 #since previous lines dealt with the divisabilty of 2 and 3 making the variable equal to 5 should take care of the rest.
    while i * i <= num: # this loop continues as long as the number inputed is less than or equal to the inputed number. so the input can't be greater than i as a number can't have a divisor greater than it's square root.
        if num % i == 0 or num % (i+2) == 0: # this checks for numbers divisable by i and numbers diviasble by i+2, if they can be divided by these two numbers return false.
            return False 
        i += 6 # increments by 6
    return True    