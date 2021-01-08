"""
This exercise function that converts numeric numbers into Roman with up to 9999,
using as little pre-made roman numbers and as much logic as possible
|V = 5000
|X = 10 000
"""


def make_roman(I_number = 0):
    if not I_number:
        # Making sure I_number is an integer and between 0 and 9999
        while True:
            print("Input number up to 9999:")
            I_number = input()
            try:
                I_number = int(I_number)
                if not 0 <= I_number <= 9999:
                    continue
                break
            except:
                print("Should be an integer up to 9999")

    # Array for storing digits of numeric number
    I_digits = []

    # saving digits in array
    for digit in str(I_number):
        I_digits.append(int(digit))

    # saving digits in array named for numeric thousands (m) hundreds (c) tens (x) and singles (i)
    N_m = I_digits[len(I_digits) - 4] if I_number >= 1000 else 0
    N_c = I_digits[len(I_digits) - 3] if I_number >= 100 else 0
    N_x = I_digits[len(I_digits) - 2] if I_number >= 10 else 0
    N_i = I_digits[len(I_digits) - 1]

    # declaring empty strings for roman thousands (m) hundreds (c) tens (x) and singles (i)
    R_m = ''
    R_c = ''
    R_x = ''
    R_i = ''

    # processing thousands
    if 1 <= N_m <= 3:
        R_m = N_m * 'M'
    elif 4 <= N_m <= 8:
        R_m = ('M' if N_m == 4 else '') + '|V' + ('' if N_m == 5 else (N_m - 5) * 'M')
    elif N_m == 9:
        R_m = 'M|X'

    # processing hundreds
    if 1 <= N_c <= 3:
        R_c = N_c * 'C'
    elif 4 <= N_c <= 8:
        R_c = ('C' if N_c == 4 else '') + 'D' + ('' if N_c == 5 else (N_c - 5) * 'C')
    elif N_c == 9:
        R_c = 'CM'

    # processing tens
    if 1 <= N_x <= 3:
        R_x = N_x * 'X'
    elif 4 <= N_x <= 8:
        R_x = ('X' if N_x == 4 else '') + 'L' + ('' if N_x == 5 else (N_x - 5) * 'X')
    elif N_x == 9:
        R_x = 'XC'

    # processing ones
    if 0 <= N_i <= 3:
        R_i = N_i * 'I'
    elif 4 <= N_i <= 8:
        R_i = ('I' if N_i == 4 else '') + 'V' + ('' if N_i == 5 else (N_i - 5) * 'I')
    elif N_i == 9:
        R_i = 'IX'

    # combining different segments into ready roman number, and printing said number.
    print("Number converted to roman is")
    if I_number >= 1000:
        print(R_m + R_c + R_x + R_i)
    elif I_number >= 100:
        print(R_c + R_x + R_i)
    elif I_number >= 10:
        print(R_x + R_i)
    else:
        print(R_i)
