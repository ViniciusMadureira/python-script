### -*- coding: utf-8 -*-
__author__="Vinícius Silva Madureira Pereira <viniciusmadureira@outlook.com"
__date__="$Dez 2, 2017 5:03:09 AM$"

from string import ascii_lowercase, digits

base_list = None

def set_base_list(base):
   global base_list
   base_list = ([str(value) for value in digits] + [str(value) for value in ascii_lowercase])[0:base]

def convert(number, current_base, new_base):
    if(is_valid_base(current_base) and is_valid_base(new_base) and is_valid_number_for_base(number, current_base)):
        decimal_base = number if current_base == 10 else to_decimal(number, current_base)
        return decimal_base if new_base == 10 else from_decimal(decimal_base, new_base)

def is_valid_base(base):
    if 2 <= base <= 36:
        return True
    print('Invalid base: {}. Base value must be >= 2 and <= 36.'.format(base))
    return False

def is_valid_number_for_base(number, base):
    number = str(number).lower()
    set_base_list(base)
    for index in range(len(number)):
        if (number[index].lower() not in base_list):
            print('{} is invalid to base {}.'.format(number, base))
            return False
    return True

def to_decimal(number, base):
    number = str(number).lower()[::-1]
    total = pot = 0
    for index in range(len(number)):
        total += base_list.index(number[index]) * base ** pot
        pot += 1
    return total
    
def from_decimal(number, base):
    rest_list = ''
    set_base_list(base)
    while number > 0:
        rest_list += base_list[number % base]
        number = int(number / base)
    return rest_list[::-1]

print(convert(60, 10, 16))
