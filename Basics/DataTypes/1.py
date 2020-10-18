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