"""from sys import last_traceback


print('my name is\n vishal')
print('name\t m.no\t country')
print('vishal\t 1214\t india')
print('vishal\t 1224\t india')
print('akshay\t 1224\t india')



first_name = 'vishal'
last_name = 'dhiman'
language = 'Python'
formated_string = 'I am {} {}. I learn {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))



# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal

print(formated_string)"""

from platform import python_branch


first_name ='vishal'
last_name ='dhiman'
formated_string = 'my first name {} and last name is {}' .format(first_name, last_name)
print(formated_string)

language = 'python'
a,b,c,d,e,f = language
print(a) 
print(b) 
print(c) 
print(e) 
print(f)

print(a,' ', b,' ', c, ' ', d, ' ', e, ' ', f)

language = 'python'
first_letter = language[5]
print(first_letter)
