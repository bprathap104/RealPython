"""
Variable Assignment - No need to define types
"""
n = 300
print(n)

n = 400
print(n)

n = 'hello'
print(n)

m = n = x = y = 100  ## Chained Assignment
print(m)
print(n)
print(x)
print(y)

a, b = 300, 400      ## Multiple Assignment, no. of variables in left side & no. of values on right side should be same
print(a)
print(b)

n = 300
print(type(n))
n = "hello"
print(type(n))

"""
Object references - Everything in Python is an Object
"""
## Everything in python is an object
## Variables are references of objects
## Orphaned objects -> variables pointing to different objects

"""
Object Identity
"""
n = 300
print(id(n))
m = 300
print(id(m))


print(n == m)  ## Returns True
print(id(n) == id(m)) ## Returns False


"""
Small Integer Caching
"""
## Python cachces small integers -5, -4, -3, ..... 254,255, 256

n = 30
print(id(n))
m = 30
print(id(m))


print(n == m)  ## Returns True
print(id(n) == id(m)) ## Returns True as well

## Python pub quiz question
a, b = 250, 250

for _ in range(250, 260):
    if a is not b:
        break
    a += 1
    b += 1
print(a)

# Above program return 257

"""
Variable Names
# Any length allowed
# Upper case characters allowed
# Mixed case characters allowed
"""
this_is_a_really_really_really_long_name = 40
CONSTANT = 40
MIxmeNOT = 20
print(this_is_a_really_really_really_long_name)
print(CONSTANT)
print(MIxmeNOT)
num_videos = 10
print(num_videos)
has_w3 = 10
print(has_w3)
## 1080_w3 = 20 #Variable name starting with integer is not allowed
## Unicode is allowed in variable name

"""
Variable Names
PEP-8
"""
## https://www.python.org/dev/peps/pep-0008/



