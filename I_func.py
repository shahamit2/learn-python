# Default value is None.
def func1():
    print("Hello, World")

x = func1()
print(x)

# Multiple value returned by function.
def func1(a, b):
    return a+b, a/b

x = func1(3,2)
print(type(x)) # Tuple

# Keyword argument
def func1(name, age):
    print("{}'s age is {}".format(name, age))

x = func1("eckhart",49)
y = func1(49, "eckhart")
z = func1(age=49, name="eckhart")

# default argument
def func1(name, msg="Hello"):
    print("{},{}".format(msg,name))

x = func1("eckhart", "hi")

# Variable length args
def func1(*n):
    # can't do n[0] = 1 -- because tupple is immutable.
    print(type(n))

x = func1(2,3,4,5)
# what is a = 2,3,4,5 i.e. tuple

# Dict variable length args i.e. keyword variable args.
def func1(**n):
    print(type(n))

x = func1(n1="Python", n2="Go")

# Global variables and functions - 1
lang = "Python"

def func1():
    print("Everyone likes {}".format(lang))

#  Global variables and functions - 2
def func1():
    global lang
    lang = "python"

def func2():
    print("Everyone likes {}".format(lang))

func1()
func2()
globals() # Built in function.

# Lambda
# lambda args : expression
s = lambda name,msg : print("{} , {}".format(name,msg))
s("eckhart", "hello")
# lambda use
map_obj = map(lambda l: l*2,[1,3,5])
for mo in map_obj:
    print(mo)

# Function as argument.
def iseven(x):
    if x%2 == 0:
       return True
    return False

def isodd(x):
    if x%2 != 0:
       return True
    return False

def filterlist(func, list):
    newlist = []
    for l1 in list:
        if func(l1):
            newlist.append(l1)
    return newlist

list = [1,2,3,4,5,6,7,8]
listeven = filterlist(iseven, list)
listodd = filterlist(isodd, list)
print("List : {}".format(list))
print("List even : {}".format(listeven))
print("List odd : {}".format(listodd))

# Decorator
# Decorate your function with adding some more processing to it.
# Simple Example for Decorators
# Function accepting function and returning function is decorator function.
def dec(in_func):
    def ret_func():
        print("{:*>50}".format(""))
        in_func()
        print("Decorating plain functions..")
        print("{:*>50}".format(""))
    return ret_func

@dec
def plain_func():
    print("plain_func: this needs to be decorated..")

# This is not same 'plain_func' because decorated.
# This is 'ret_func' returned by 'dec'
plain_func()

# Example 2 of decorator.
def outer(func):
    def inner(name):
        print("Welcome Welcome")
        func(name)
    return inner

@outer
def guest(name):
    print("{}, you are great teacher".format(name))

guest("eckhart")



# Generators
def bigint():
    for i in range(1000000):
        yield i

b = bigint()
print(type(b))
next(b)

################################################################
# Iterator
# Working of iterators
# Python iterator object must implement two special methods, \
# \ __iter__() and __next__(), collectively called the iterator protocol.
# The iter() function (which in turn calls the __iter__() method) returns \
# \ an iterator from them.

# Inbuild example of list.
my_list = [4, 7, 0, 3]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())

for element in my_list:
    print(element)

# Build class with iterator methods.
class PowTwo:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# Way 1
for i in PowTwo(5):
    print(i)

# Way 2
a = PowTwo(4)
i = iter(a)
next(i)
next(i)


################################################################
# Closure not working in Python
def increment():
    num = 1
    def retinc():
        i = num + 2
        print(i)
    return retinc

x = increment()
x()
x()

# Closure in GO.
package main

import "fmt"

func increment() func() {
    num := 0
    return func() {
        num = num + 1
        fmt.Printf("num : %d\n",num)
    }
}

func main() {
     inc := increment()
     inc()
     inc()
     inc()
}
