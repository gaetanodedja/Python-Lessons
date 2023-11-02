
"""Funxions"""
def square (x):
    return x*x

square(10)


def nth_root(radicant, n):
    return radicant ** (1/n)

nth_root(27,3)

import wordsFromURL
wordsFromURL.fetch_words()

m = [9, 23, 31]

def modif(k):
     k.append (39)
     print (k)

modif(m)


"""Modules"""
import time
def show_time(arg=time.ctime()):
    print(arg)

show_time()

def  add_menu (menu = None):
    if menu is None:
        menu = []
    menu.append("item")
    return menu

breakfast = ["Egg","Milk","Waffle"] 
add_menu(breakfast)

import wordsFromURL
type(wordsFromURL)
dir(wordsFromURL)


"""Tuples"""
def minmax (items):
    return min (items), max (items)

minmax([22,1,0,56,47])

"""strings"""

colors = ';'.join(['#45ff23', '#2321fa','#1298a3'])
colors

colors.split(';')
colors


start, _, destination = "Tirana-Elbasan".partition('-')
start 
destination


"Favorite team of {0} is {1}".format('GD','Liverpool')
"Geo position is L:={pos[0]}, La:={pos[1]}".format(pos=("60N","23.0"))

value = 2 * 15
f'The value is {value}'

import datetime
import math
f'The current time is {datetime.datetime.now().isoformat()}'
f'Pi number is {math.pi:.3f}, E number is {math.e:.3f}'

help (str)

"""Range"""
range(2,10)
for i in range(2,10):
    print(i)

list (range(2, 10, 2))

l = [1,3,6,8,11]
for i in range (len(l)):
    print(l[i])

l = [1,3,6,8,11]
for i in l:
    print(i)

"""string list"""
h = 'I love footbal and liverpool as a team'.split()
h
h.sort(key=len)
h
' '.join(h)

"""Dictonaries"""

sites = {'Google': 'http://google.com',
         'Facebook':'http://facebook.com',
         'Pluralsight': 'http://pluralsight.com',
         'Microsoft': 'http://microsoft.com'}

sites['Microsoft']

sites['Udemy'] = 'http://udemy.com'

sites 

for site in sites:
    print (f"{site} => url of the site is: {sites[site]}")

"""sets are the same as dict but contains single value"""
p =  {5, 90, 21, 2} 

e = set()
e.add(23)
e


splitList = h = 'I love footbal and liverpool as a team'.split()
splitList

[len(words) for words in splitList]

from math import factorial
s = {len(str(factorial(x))) for x in range(20)}
s

sites = {'Google': 'http://google.com',
         'Facebook':'http://facebook.com',
         'Pluralsight': 'http://pluralsight.com',
         'Microsoft': 'http://microsoft.com'}

sites = {url: web for web, url in sites.items()}
sites #inverted the key

words = ['hi', 'hello', 'fox', 'dog']

{x[0]: x for x in words}

"""iterator"""
from math import sqrt

def is_prime(x):
    if x < 2:
       return False
    for i in range (2,int(sqrt(x)) + 1):
        if x % 1 == 0: 
            return False
    return True     

[x for x in range(101) if is_prime(x)]

prime_square_divisors = {x*x: (1, x, x*x) for x in range(20) if is_prime(x)}
prime_square_divisors

def first (iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

first(words)

"""Generator functions"""

def gen123 ():
    print("About to yield 1")
    yield 1 
    print ("About to yield 2")
    yield 2
    print ("About to yield 3")
    yield 3

generator = gen123()

for gen in gen123():
    print(gen) 


"""Classes"""
from aircrafts import flight

fl = flight("AA1234")

from aircrafts import Aircraft

a = Aircraft ("G-EUPT", "Airbus A319", num_rows=12, num_seats_per_row= 5)

a.model() #attribute from class

a.seating_plan()  #method from class


from aircrafts import *

fly = flight("AA777", Aircraft("G-EUPT", "Airbus A319", num_rows = 12, num_seats_per_row = 5)) #merr 2 argumente , tek argumenti dyt i kemi dhene klasen Aircraft

fly.aircraft_model()
