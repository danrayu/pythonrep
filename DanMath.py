import math

from InputQualifier import input_checkif_number


def law_of_sines():

    type_of_action = input("Type in if you know 2 sines or 2 lengths (sin/len):")

    if type_of_action == 'sin':
        print("You know 2 sines and 1 length. sin(A), length a, and sin(B):")
        a = input_checkif_number("Type in angle A:")
        length_a = input_checkif_number("Type in length a:")
        b = input_checkif_number("Type in angle B:")
        length_b = math.sin(math.radians(a))/length_a/math.sin(math.radians(b))
        print('Length b = {}'.format(length_b))

    elif type_of_action == 'len':
        print("You know 1 sine and 2 lengths. sin(A), length a, length b:")
        a = input_checkif_number("Type in angle A:")
        length_a = input_checkif_number("Type in length a:")
        length_b = input_checkif_number("Type in length b:")
        b = math.asin(math.sin(math.radians(a))/length_a*length_b)
        print('Angle B = {}'.format(math.degrees(b)))
    else:
        print("WRONG")
        law_of_sines()
        return
