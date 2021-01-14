print("string:")
str1 = input()
print("char:")
char = input()
starts_with = lambda str, char: str[0] == char

print(starts_with(str1, char))