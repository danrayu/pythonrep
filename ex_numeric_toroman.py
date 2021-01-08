"""
This exercise converts numeric numbers into Roman with up to 9999,
using as little memory and as much logic as possible
"""
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

I_digits = []
for digit in str(I_number):
    I_digits.append(int(digit))

I_m = I_digits[len(I_digits) - 4] if I_number >= 1000 else 0
I_c = I_digits[len(I_digits) - 3] if I_number >= 100 else 0
I_x = I_digits[len(I_digits) - 2] if I_number >= 10 else 0
I_i = I_digits[len(I_digits) - 1]

R_m = ''
R_c = ''
R_x = ''
R_i = ''

if 1 <= I_m <= 3:
    R_m = I_m * 'M'
elif 4 <= I_m <= 8:
    R_m = ('M' if I_m == 4 else '') + '|V' + ('' if I_m == 5 else (I_m - 5) * 'M')
elif I_m == 9:
    R_m = 'M|X'

if 1 <= I_c <= 3:
    R_c = I_c * 'C'
elif 4 <= I_c <= 8:
    R_c = ('C' if I_c == 4 else '') + 'D' + ('' if I_c == 5 else (I_c - 5) * 'C')
elif I_c == 9:
    R_c = 'CM'

if 1 <= I_x <= 3:
    R_x = I_x * 'X'
elif 4 <= I_x <= 8:
    R_x = ('X' if I_x == 4 else '') + 'L' + ('' if I_x == 5 else (I_x - 5) * 'X')
elif I_x == 9:
    R_x = 'XC'

if 0 <= I_i <= 3:
    R_i = I_i * 'I'
elif 4 <= I_i <= 8:
    R_i = ('I' if I_i == 4 else '') + 'V' + ('' if I_i == 5 else (I_i - 5) * 'I')
elif I_i == 9:
    R_i = 'IX'

if I_number >= 1000:
    print(R_m + R_c + R_x + R_i)
elif I_number >= 100:
    print(R_c + R_x + R_i)
elif I_number >= 10:
    print(R_x + R_i)
else:
    print(R_i)
