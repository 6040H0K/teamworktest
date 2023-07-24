import math

inp_int = int(input('Your value: '))

def sinus(number):
    sin_num = math.sin(number)
    return sin_num

sin_print = sinus(inp_int)
print(f'Sinus of your value is: {sin_print}')
