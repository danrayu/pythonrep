"""
Exercise: Write a program that checks if the reverse of a number is the same number.
It mustn't accept anything except numbers
"""
split_original_number = []
split_reversed_number = []

while True:
    print("input number:")
    number = input()
    try:
        int(number)
        break
    except:
        print("should be an integer!")

for digit in str(number):
    split_original_number.append(digit)
    split_reversed_number.insert(0, digit)

if split_reversed_number == split_original_number:
    print("Yes, it is equal to the reverse")
else:
    print("No, it isn't equal to the reverse")
