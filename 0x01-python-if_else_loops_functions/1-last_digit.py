#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigitVal = number % 10
lastDigitSign = 1 if number > 0 else -1

lastDigit = lastDigitVal * lastDigitSign
returnString = "Last digit of " + str(number) + " is " + str(lastDigit)

if (lastDigit > 5):
    returnString += " and is greater than 5"
elif(lastDigit == 0):
    returnString += " and is 0"
elif(lastDigit < 6 and lastDigit != 0):
    returnString += " and is less than 6 and not 0"

print(returnString)
