##############Arithmetic Operators##############
a = 10
b = 20
print(a + b)
print(a + b - 5)
print(+a)       # unary positive
print(-b)       # unary negation
print(a - b)
print(a * b)
print(a / b)    # always return a float
print(type(a / b))    # always return a float
print(a % b)
print(a ** b)   # a to the power b, exponentiation
print(b // a)   # Floor division returns integer
                # Round of to nearest small integer

###############Comparison Operators##############
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
x = 1.1 + 2.2
print(x == 3.3)  # This will return False, as float arithmetic can't be relied upon
tolerance = 0.00001
print(abs(x - 3.3) < tolerance) # This returns True

###############Logical Operators##############
x = 5
y = 2
print(x < 10)
print(type(x < 10))
t = x > 10
print(type(t))
callable(x)                 # Returns false as x is not callable
print(type(callable(x)))    # Returns bool
## not, and, or
print(not x)                # Returns False if x is True and vice versa
print(x or y)               # Returns True since x or y is integers
print(x and y)              # Returns True since x and y is integers

x = 5
print(not x < 10)           # Returns False
print(not callable(x))      # Returns True, when passing a variable to callable, returns false

x = 5
print(x < 10 or callable(x))
print(x < 0 or callable(x))

x = 5
print(x < 10 or callable(x))
print(x < 10 or callable(len))

print(bool(0),bool(0.0),bool(0+0.0j))  # All returns False
print(bool(-2),bool(3.14159),bool(1+1j))    # All Returns True, as non-zero

print(bool(''),bool(""),bool(""""""),bool('''''')) # Returns False as empty strings
print(bool(' '),bool("foo"),bool(''' ''')) # Returns true

print(bool([]))  # Returns false for an empty list
print(bool([1,2,3])) #Returns true for an non empty list

print(bool(None)) # Returns False

x = 2
y = 4
print(x or y)   # Returns 2 and not True **** truthy

x = 0.0
y = 4.4
print(x or y)   # Returns 4.4 as x = 0.0. Again it doesn't return False ****

x = 3
y = 4
print(x and y)  # Returns y as it evaluates both x and y for truthinees

x = 0.0
y = 4.4
print(x and y)  # Returns x as it evaluates to falsy



