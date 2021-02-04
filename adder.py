import math

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# odinakowie=[]
# odinakowie2 = []
# for number in a:
#     for number2 in b:
#         if number==number2:
#             odinakowie.append(number)
#
# for occurence in odinakowie:
#     if odinakowie.count(occurence) > 1:
#         odinakowie.remove(occurence)
# print(odinakowie)


# y_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# dict = y_dict.values()
# max_number=0
# for key in dict:
#     if key > max_number:
#         max_number=key
# print(max_number)



# print(int('ABC', 16))



# slovo=input(">")
# if slovo[::-1]==slovo:
#     print("da")
# else:
#     print("net")

# seconds = int(input("seconds:"))
# hours = seconds // 3600
# print(hours)




"""
list=[1,2,3,4,5,6]
print(list[0],list[-1])"""

# import os
# dir = input()
# dir = dir[::-1]
# index = 0
# for char in dir:
#     if char == '.':
#         print(dir[:index][::-1])
#     index += 1



# number="1"
# number2=number*2
# number3=number*3
# output=int(number)+int(number2)+int(number3)
# print(output)


# a=[1,2,3,4,6,7,10]
# b=[11,12,13,14,1]
# uniques=[]
# for number in a:
#     if number not in b:
#         uniques.append(number)
# print(uniques)


# import os
# print(list(os.scandir()))

# number2 = []
# readynumber = 0
# number="11"
# for char in number:
#     number2.append(char)
# for number1 in number:
#     readynumber += int(number1)
# print(readynumber)


# def find_char(char):
#     stroka="1123456"
#     index=0
#     for number in stroka:
#         if number==char:
#             index+=1
#     print(index)
# find_char(input(">"))


# x=5
# y=10
# z=0
# z = y
# y = x
# x = z
# print(y,x)
string = [13, 14,15, 30]
lambdaf = lambda stri: stri % 15 == 0
divis15 = filter(lambdaf, string)
for x in divis15:
    print(x)







