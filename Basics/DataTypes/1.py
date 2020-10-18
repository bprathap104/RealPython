""""
Integers
"""
a = 3
c = 0b101010111
print(c)
d = 0o454312
print(d)
e = 0xac4d
print(e)
f = '12345'
print(f)
print(int(f))
print(type(a))
""""
Floating point numbers
Division always gives float numbers
"""
a = 10
b = 4
print(a / b)
print(a // b)
j=4e3
print(j)
print(4e-3)
a = 0.2
b =0.1
c = a + b
print(c)
""""
Complex Numbers
"""

a = 2+3j
b = 4+5j
print(type(a))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
""""
String
"""
a = 'He said "i wasn\'t available for class today"'
print(a)
b=r"One Line\nTwo Line"
print(b)
"""
Triple-quoted-String
"""


"""
Booleans
"""
a = 2
print(type(a))
print(bool(a))

a = 2
print(a == 2)
b = 2 
print(b == 0)
if b:
    print('B is true!')
else:
    print('B is false!')

b = False 
if b:
    print('B is true!')
else:
    print('B is false!')

b = [] 
if b:
    print('B is true!')
else:
    print('B is false!')

b = {} 
if b:
    print('B is true!')
else:
    print('B is false!')


"""
Functions - Composite Data Types
List & Tuple
"""
a = [1,2,3,4,5]   ## List
print(a[-1])
print(a[1:3])
a[1] = 6
print(a)

b = (1,2,3,4,5)   ## Tuple
print(b[0])
print(b[-1])
print(b[1:3])
## b[1] = 6  ## This is not allowed in tuple
"""
Functions - Composite Data Types
Set - A set is a data structure that can contain only unique elements
"""
a = [1,2,3,3,3,4]
print(a)
b = set(a)
print(b)
c=list(b)
print(c)

"""
Functions - Composite Data Types
Dict - Lookup table
"""
a = dict()
a['age'] = 48
a['name'] = 'Darren'
print(a)
print(a['age'])
## print(a['country']) # This will give a key error as 'country' is not defined
print(a.get('country'))


"""
Functions - Composite Data Types
Math
"""
print(abs(5))
print(abs(-5))
print(15 // 4)
print(15 % 4)
print(divmod(15, 4))
print(max([1,2,3,4,5]))
print(max([-4,-2]))

print(min([1,2,3]))
print(min([-4,-2]))

print(pow(3,2))
print(3 ** 2)
## pow(3,2,2) = 3 ** 2 % 2
print(pow(3,2,2))
print(round(4.5))
print(round(4.6))
print(int(4.5))
print(int(4.6))
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],10))

"""
Functions - Type Conversion
"""
print(ascii("hello"))      ## ASCII -> Americal standard code for Information Interchange
print(ascii("'ôæ"))
print(chr(244))            ## chr works for both ascii & unicode characters
print(chr(0x06a4))
print(ord('a'))              ## ord is complementary to chr function. ord does convert any character into ascii
print(type('a'))
print(type(2))
print(type('hello'))
print(type(4.0))
print(type(True))
print(type([1,2,3,4,5]))
print(int('1234'))
print(int('1234', base=16))
print(int('1010', base=2))
print(bin(10))
print(oct(10))
print(hex(10))
print(float(4))
print(complex(10))
print(complex(4+3j))
print(str(1234))
print(bool(0))
print(bool(1))
print(bool(1234))
"""
Functions - Iterables & Iterators
"""
a = [1,2,3,4,5,6]
print(len(a))
a = [True, True, True]
b = [True, False, True]
c = [False, False, False]

print(any(a))
print(any(b))
print(any(c))
print(all(a))
print(all(b))
print(all(c))

d = [1,2,4,7,3,9,22]
print(len(d))
e = reversed(d)
print(e)
print(list(e))
f = sorted(d)
print(f)

a = range(10)
print(a)
print(list(a))
print(list(range(10)))
print(list(range(0,10,2)))

"""
Functions - Iterables & Iterators
Enumerate
"""
players = ['bob', 'bryan', 'tim', 'cook']
counter = 0
for player in players:
    print(counter, player)
    counter += 1

for count, player in enumerate(players):
    print(count, player)

"""
Functions - Iterables & Iterators
zip
"""
number_list = [1,2,3,4,5,6]
alpha_list = ['a','b','c','d','e','f']

merged = []
for i in range(len(number_list)):
    merged.append((number_list[i], alpha_list[i]))
print(merged)

merged_1 = zip(number_list, alpha_list)
print(merged_1)
print(list(merged_1))


"""
Functions - Iterables & Iterators
Iter & Next
"""
a = iter([1,2,3,4,5,6])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
## print(next(a))   # This will produce stopiteration as list is exhausted


"""
Functions - Input & Output
print
"""
for i in range(100):
    print(i)
for i in range(100):
    print(i, end=' ')
print()

"""
Functions - Input & Output
open
"""
file = open('test.txt', 'w')
file.write("Hello World\n")
file.close()

file = open('test.txt', 'r')
print(file.readlines())
file.close()

"""
Functions - Variables, References & Scope
Part-1 - DIR
"""
a = 'hello'
print(a.upper())
print(a.capitalize())
dir(a)                      ## dir works with any kind of objects in python
print(a.center(50))
import datetime
dir(datetime)
dir(datetime.datetime)

"""
Functions - Variables, References & Scope
Part-2 - Vars & Globals
"""
a = 1
b = 'global'
c = 'another global'

def function():
    a = 2
    b = 'local'
    print(a, b)

print(a, b)
function()
print(a, b)
####### 

a = 1
b = 'global'
c = 'another global'

def function():
    a = 2
    b = 'local'
    print(a, b)
    print(vars())

print(a, b)
function()
print(a, b)
print(globals())


"""
Miscellaneous
Exec
"""
# import os
# job = input("Enter you job to execute: ")
# exec(job, {"pow": pow})
## This allows only pow function to be called

"""
Miscellaneous
Hash
"""

print(hash(123456))
print(hash('Hello world from Real Python!'))
print(hash('Hello world from Real Python.'))

with open('Pipfile','r') as file_obj:
    pip_list = file_obj.readlines()

pip_1 = ''.join(pip_list)
pip_2 = ''.join(pip_list)

print(hash(pip_1) == hash(pip_2))   ## Returns True

pip_2 += ' '

print(hash(pip_1) == hash(pip_2))   ## Returns False