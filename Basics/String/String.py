## String Operators:
## +(concatination), *(duplicates n times)
s = 'spam'
t = 'egg'
u = 'bacon'
print(s + t + u)
print('Go Team' + '!!!')
n = 2
print(s * n)
n = 8
print(s * n)
s = 'spam.'
print(s*n)
print('bacon' * -7)  ## When multiplying by 0 or negative numbers string becomes null string

## Memebership Operators (in, not in)
s = 'spam'
print(s in 'I saw a spam a lot')       # Returns True
print(s not in 'I saw a Holy Grail!')  # Returns True
s = 'I saw'
print(s not in 'I saw a Holy Grail!')  # Returns False

# Built-in Methods
print(ord('a'))  # Returns Unicode equivalents
print(ord('#'))  # Returns Unicode equivalents
print(chr(97))   # Returns Alpha/Special character/Integer for Unicode
print(chr(35))   # Returns Alpha/Special character/Integer for Unicode
print(chr(129363))
s = 'I am a string'
print(len(s))
s = ''
print(len(s))
print(str(49.2))
print(str(3 + 29))
a = str(3+29)
print(type(a))

## String Indexing
s = 'mybacon'
print(s[0])
print(s[1])
print(s[2])
print(s[len(s) - 1])
print(s[-1])            # Returns last character
print(s[-len(s)])       # Returns first character

### String Slicing   s[m:n] starting with 'm' and not including 'n'
s = 'mybacon'
print(s[2:5])   #Returns 'bac'
print(s[2:7])   #Returns 'bacon'
print(s[0:3])   #Returns 'myb'
print(s[0:2])   #Returns 'my'
# Omitting the first and/or last index
# s[:n],s[m:],s[:]
print(s[:2])    #Returns 'my'
print(s[:5])    #Returns 'mybac'
print(s[2:])    #Returns 'bacon'
print(s[2:len(s)])  #Returns 'bacon'
print(s[:2])    # Returns 'my'
print(s[:2] + s[2:]) #Returns 'mybacon'
print(s[:4] + s[4:]) #Returns 'mybacon'
print(s[:])     # Returns 'mybacon'
t = s[:]
print(id(t))
print(id(s))
print(s == t)   #True
print(s is t)   #True
print(s[2:2])   #''
print(s[4:2])   #'' #Here m is greate than n
print(s[-5:-1]) #'baco'
print(s[0:7:2]) #'mbcn' #:2 is for step
print(s[1:7:2]) #'yao'
s = '12345' * 5 #1234512345123451234512345
print(s[::5])   #11111
print(s[4::5])  #55555
print(s[::-5])  #55555
print(s[::-1])  #5432154321543215432154321
s = 'tacocat'
s == s[::-1]    #Polyndrome, Returns True

### Interpolating variables into a string
n = 20
m = 25
prod = n * m
print('The product of ', n, 'and', m, 'is', prod)
print(f'Th product of {n} and {m} is {prod}')
print(f'Th product of {n} and {m} is {n * m}')     ## ''', """, f, F all allowed
print(F'''The product of 
                         {n}
                         {m}
                         {prod}
''')

## Modifying strings
