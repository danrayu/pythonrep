import enum

""" ex 1 print name and value of enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


for country1 in Country:
    print(country1.name)

for country in Country:
    print(country.value)
"""

from enum import IntEnum


class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


country_code_list = list(map(int, Country))
print(country_code_list)
