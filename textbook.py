# function types

def say_hello():
    print("Hello")


def give_back(x):
    return x


# variables from outer scope can be read, but not changed
y = 5


def return_from_outer():
    return y


# bad example: having things shadowing names in different scopes
# y = 2
# def set_y(num):
#     y = num
#


# my bool is of type bool
x = 2
my_bool = x == 2

# example of use of functions and bool and while
from InputQualifier import input_compare_w_string


def market():
    three_groceries = []
    groceries = ["apple", "book", "meat", "rice", "hot sauce"]

    while len(three_groceries) < (3 if len(groceries) >= 3 else len(groceries)):
        grocerie = input_compare_w_string(
            "Select one of these groceries: Apple, Book, Meat, Rice, Hot sauce:\n", "Good. Next grocerie:", groceries) \
            .lower()
        three_groceries.append(grocerie)

    print("You have to but these 3")
    for g in three_groceries:
        print(g)


def return_pizza_slice(slice_start, slice_end):
    print("pizza"[slice_start:slice_end])


# code running the selection of functions
commands_list = ["continue", "market", "pizza"]
commands_string = ""
for command in commands_list:
    commands_string += command + "/"

commands_string = commands_string[0:(len(commands_string) - 1)]

#command = input_compare_w_string("type in command (" + commands_string + "):", "", commands_list).lower()

if command == "market":
    market()
elif command == "pizza":
    return_pizza_slice(0, 2)


# class example
class DogExample:
    age = 0
    name = ""

    def print_info(self):
        print("age: " + str(self.age) + ", name: " + self.name)


dog1 = DogExample()
dog1.name = "Oy"
dog1.age = 5


# dog1.print_info()


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_info(self):
        print("age: " + f'{self.age}' + ", name: " + self.name)


dog2 = Dog("Goddog", 2)


# dog2.print_info()


# class inheritance example
class Pug(Dog):
    def __init__(self, name: str, age: int, sound: str):
        super().__init__(name, age)
        self.sound = sound

    def make_noise(self):
        print(self.sound)


pug = Pug("Lard", 2, "Grrhhhhhaaahhh")
# pug.print_info()
# pug.make_noise()
