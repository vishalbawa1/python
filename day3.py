from itertools import product

#from exerciseday2 import Radius


a = 5
b = 3

total = a+b
diff = a-b
pro = a*b
division = a/b
remainder = a%b
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', pro)
print('a / b = ', division)
print('a % b = ', remainder)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations

total = num_one+num_two
print(total)

#calculate (area, volume,density, weight, perimeter, distance, force)
Radius = 30
area_of_circle = 3.14*Radius ** 2
print('area of circle =', area_of_circle)

length = 10
weidth = 20
area_of_rectangle = length * weidth
print('area of rectangle =',area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density)

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


print('Floating Point Number, PI', 3.14)
print('Multiplying complex numbers: ',(5 + 3j) * (1 - 1j))

