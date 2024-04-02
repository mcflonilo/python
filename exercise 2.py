import pandas as pd
import numpy as math
x = 2.5
y = -1.5
m = 18
n = 4
#a
n=1
m=-1
if n<-m :
    print(n)
else :
    print(m)

#b
if -n >= m :
    print(n)
else:
    print(m)
    
#c
x=0.0
y=1.0
if abs(x-y)<1:
    print(x)
else:
    print(y)
    
#d
x=math.sqrt(2.0)
y=2.0
if x*x == y:
    print(x)
else:
    print(y)
""" 
#oppgave 2
x = int(input())
if  x>10:
    print("høyere")
elif x<=10|x>=1:
    print("mellom")
else:
    print("mindre")
"""
#oppgave 3
print("skriv tall")
x = int(input())
if x>=90:
    print("A")
elif x>=80:
    print("b")
elif x>=70:
    print("c")
elif x>=60:
    print("d")
else:
    print("f")