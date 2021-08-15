"""
Exercise: Write a program that checks if the reverse of a number is the same number.
It mustn't accept anything except numbers
"""

from InputQualifier import input_check_if_int

number = input_check_if_int(message = "Type in a number:")

if number == number[::-1]:
    print("Reversible.")
else:
    print("Not reversible.")
