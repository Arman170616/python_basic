#Check int
a=2
print(a)   
print(type(a))

#Check int
b=922337203685477807
print(b)                
print(type(b))

 #Floating point
pi=3.14
print(pi) 
print(type(pi))

 #sting
name = 'Jhon Deo'
print(name)   
print(type(name))


 #Boolean
x = True
print(x) 
print(type(x))


#Null data type
x=None
print(x)  
print(type(x))

#Show python keywords
import keyword
print(keyword.kwlist)


#demo function
x,y,z = 10,5,4
def mulfunc():   
    p = x*y+z
    print('the value of p is:',p)
mulfunc()

#

def my_function():
    a = 2
    return a
print(my_function())


#tuple:An ordered collection of n values of any type(n> =0)

a = (1, 2, 3)
b = ('a', 1, 'python',(1, 2))    
b[2] = 'else'


#list:An ordered collection of  values(n> = 0)
a = [1, 2, 3]
b = ['a', 1, 'python', [1,2]]    
b[2] = 'esab'
print(b[2])
print(b)
#ValueError: invalid literal for int() with base 10: '123.456'
a = '123.456'
b = float(a)
d = int(b)
print(b)  
print(d)


a = 'hello'
print(list(a))
print(set(a))
print(tuple(a))

def f(m):
    m.append(3)   # adda a number to the list .This is a mutation..

x = [1, 2]
f(x)
x == [1, 2]      #False now,since an item was added to the list..
print(x)


#  Collection Types

 #Lists
int_List = [1, 2, 3]
print(int_List)

string_List = ['hello', 'Arman']
print(string_List)

#empty list
empty_list=[]   
print(empty_list)

mixed_List = [1, 'abc', True, 2.35, None]
print(mixed_List)


#Nested_list
Nested_list = [['a', 'b', 'c'],[1, 2, 3], 2]
print(Nested_list[2])
print(Nested_list)




names = ['arman','mahdi','nafiul','maruf','tahsin']
#print(names[1])
#print(names[4])
#print(names[-1])
#print(names[-4])

#names.append('tania')
names.insert(1,'aladin')
print(names)

import math
a = math.sqrt(16)
print(a)


names = ['a','b','c']
print(names[2])
print(names[-1])
names.append('d')
print(names)
names.insert(1,'s')
print(names)

names.remove('c')
names.index('b')
print(names)

#count length of list
a = len(names) 
print(a)



#count occurrence of any item in list
a = [1, 1, 1, 2, 3, 4]
a.reverse()            #Reverse the list
a[::-1]              #or
#print(a)

a.pop(0)     #pop index pos
print(a)


#tuple
ip_adresss = ('10.20.30.40',8080)
print(ip_adresss)
print(type(ip_adresss))

one_member = tuple(['one_member',])
print(one_member)



#Dictionaries
state_capitals = {

    'dhaka' : 'bangladesh',
    'delli' : 'india',
    'nework': 'usa'
}

ca_capital = state_capitals['dhaka']
print(ca_capital)


for k in state_capitals.keys():
    print('{} is the capital of {}' .format(state_capitals[k],k))



#User_Input(Interactive input)

name = input('what is your name?')
print(name)

x = input('write a number:')

float(x)/2
print(int(x)/2)



dir(__builtins__)
#help(max)

import math
dir(math)


#chapter Tuple

t = ('a','b','c')
print(t)

t0 = ()
t1 = 'a',
t2 = ('a')
print(type(t2))


t=(1,2)
q=t
t+=(3,4)
print(t)
print(q)
g = (1, 2, 3, [1, 2, 3])
t[3] += [4,5]
print(g)


#Bulit-in Tuple Functions
tuple1 = ('a','b','c')
tuple2 = ('1','2','3')
tuple3 = ('a','b','c')



print(len(tuple1))         #3
print((max(tuple1)),(min(tuple1)))

#convert a list into tuple
list = [1,2,3,4,5]
print(tuple(list))        


tuple1 = ('a','b','c')
tuple2 = ('1','2','3')
tuple4 = (1,2,3)

print(tuple1 + tuple2)
print(tuple4[:-1])
 #reversing Elements
colors = 'red','green','blue'    
#rev = colors[::-1]
#colors = rev

rev = tuple(reversed(colors))
print(rev)





#set => sets are Unordered collections of Unique objects..two types..

basket = {'apple','mango','licci','apple','ba2na'}
print(basket)    #duplicates will be removed..
print(type(basket))

a = set('ababraded')
a.add('z')
print(a)

b = frozenset('asdfase')
print(b)
print(type(b))


#Operation on sets....
#with other sets..

#Intersection

#c = {1,2,3,4,5}.Intersection({3,4,5,6})
c = {1,2,3,4,5} & {3,4,5,6}
print(c)
{frozenset({1,2}), frozenset({3,4})}
print(d)


c = {1,2,3,4,5}
d = {3,4,5,6}

print(c.intersection(d))
print(c.union(d))
print(c.difference(d))
print(c.symmetric_difference(d))



#Chapter Dictionaries


d = {}
d = {'key': 'values'}
d = {k:v for k,v in [('key','value',)]}   #dict comprehensions..
print(d)

d = dict()
d = dict(key ='value')
d = dict([('key','value')])
d = dict(**otherdict)
print(d)



#simple Mathematical Operators

#addition

a, b  = 1, 2
print(a + b)

#import
import operator

print(operator.iadd(a,b))

name = 'arman' + ' ' + 'hossain'   #string
print(name)
num = [1,2,3] + [4,5,6]           #List
print(num)


#Exponentition

a ,b = 2, 3

c = pow(a, b)
#(a ** b)      same..
print(c)

import math
print(math.pow(a,b))


import operator
print(operator.pow(a,b))


x,y,z = 2,3,4
print(pow(x,y,z))


import math
import cmath

c = 4

print(math.sqrt(c))
print(cmath.sqrt(c))


x = 8
#print(math.pow(8, 1/3))
print(x**(1/3))


print(math.exp(0))
print(math.exp(1))


#Trigonometric Functions

import math

a, b = 1,2

print(math.cosh(b))         #inverse hyperbolic cosine of 'b' in radians..
print(math.atan(math.pi))

print(math.hypot(a, b))
print(math.sqrt(a*a +  b*b))

x1,x2,y1,y2 = 1,1,1,1

print(math.hypot(x2-x1, y2-y1))

print(math.degrees(a))
print(math.radians(57.29577951308232))


#Inplace Operations
a = 1
a += 5
print(a)


# Multiplication

c = 3 * 'xy'
d = 3 * ('a','b')
print(c)
print(d)



#bitwise Operators

print(bin(60 & 30))  #AND
print(bin(60 ^ 30))  #XOR
print((~2))          #NOT
print(bin(60 | 30)) #OR
print(bin(2 << 2))  #Left Shift
#print(2 << 2)
print(bin(8 >> 2))  #Right Shift
#print(8 >> 2)

a = 0b001
a &= 0b010
print(a)

a = 0b001
a |= 0b010
print(a)

a = 0b001
a ^= 0b010
print(a)



# nonlocal variables
def counter():
        num = 0
        def incrementer():
            nonlocal num     #UnboundLocalError: local variable 'num' referenced before assignment
            num += 1
            return num
        return incrementer

c = counter()
print(c())
print(c())
print(c())
print(c())



#global variables

x = 'hi'
 def read_x():
     print(x)
print(read_x())




#local variables
def foo():
    a = 5
    print(a)
print(a)

def f():
    if True:
        a = 5
    print(a)
b = 3
def bar():
    if False:
        b = 5
    print(b)


num = 5
if num > 2:
    print('Num is bigger than 2.')
elif num < 2:
    print('Num is smaller than 2.')
else:
    print('Num is 2.')


a = [] or 1
print(a)


def t():
    print('i am here!')
print( 0 and t())



#List


#append,extend


a = [1, 2, 3, 4, 5]
b = [8,9]
a.append(6)
a.append(7)
a.append(8)
a.append(b)
my_string = 'hello'
a.append(my_string)

a.extend(b)
a.extend(range(3))
print(a)

c =[1,2,3] + [4,5] + b
print(c)




#index,insert

a = [1,2,3,4,2,5]
b = [5,6]
#a.index(4)
#a.insert(2, 6)

#a.pop()

#a.reverse()
a.sort()
#a.sort(reverse=True)
print(a.count(2))
print(a)




#List_sort
import datetime

class person(obj):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


l = [
    person('drman', datetime.date(1997,9,26), 169),
    person('man', datetime.date(1998,9,24), 189),
    person('Aman', datetime.date(1994,9,27), 179),

]

l.sort(key = lambda item: item.name)
l.sort(key = lambda item: item.birthday)
l.sort(key = lambda item: item.height)



b = ['arman'] *3  #Replication
print(b)


a = list(range(10))
#del a[::2]
#print(a)
del a[:-1]
print(a)


lst = [1,2,3,4]
print(lst[0])


if 'a':
    print('True')
else:
    print('False')



common_divisors(12,24)
print(common_divisors(12,24))
