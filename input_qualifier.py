"""
File with different ways of qualifying the input. for example:
if input is int
if input is a digit
if input is a string
if input string has any numbers

to use uncomment the function calls
"""


#check if input is int
def check_if_int():
    while True:
        input1 = input("Enter int:")
        try:
            input1 = int(input1)
            break
        except:
            print("Isn't an int.")

#check_if_int()


#check if digit
def check_if_digit():
    while True:
        input1 = input("Enter digit:")
        if input1.isdigit():
            break
        else:
            print("Isn't a digit.")
#check_if_digit()


#check if string. input() always returns string, so it is to be used for other uses
def check_if_string():
    while True:
        input1 = input("Enter string:")
        try:
            input1 += ' '
            break
        except:
            print("Isn't a string.")
#check_if_string()


#check if any numbers are present in the string
def check_if_letters():
    number_of_numbers = 0
    input1 = input("Enter string with letters:")
    for char in input1:
        if char.isdigit():
            number_of_numbers += 1
    if number_of_numbers > 0:
        print("There", "is a number" if number_of_numbers == 1 else "are " + str(number_of_numbers) + " numbers",
              "in the string.")
    else:
        print("no numbers in string")

#check_if_letters()
