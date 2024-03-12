#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit_sign = 1 if number > 0 else -1
last_digit = number % 10 if last_digit_sign == 1 else number % -10


return_string = "Last digit of " + str(number) + " is " + str(last_digit)

if (last_digit > 5):
    return_string = return_string + " and is greater than 5"
elif (last_digit == 0):
    return_string = return_string + " and is 0"
elif (last_digit < 6 and last_digit != 0):
    return_string = return_string + " and is less than 6 and not 0"

print(return_string)
