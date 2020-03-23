import time
import mysql.connector
from mysql.connector import Error
import argparse
from random import randint
import math

parser = argparse.ArgumentParser()
parser.add_argument("Width", help="Enter lane width at the junction",
                    type=int)
arg = parser.parse_args()
W = arg.Width

t = 1
a = 15
v = 30
L = 20

h = 2.25
AmberTime = 3


V = 0
#V1 = randint(0,10)*80
#V2 = randint(0,10)*80

V1 = 1100
V2 = 800
	
V = V1 + V2
X =1.42
	
print(X)

print(V1)
print(V2)


Yc = math.floor(t + ((0.5)*(v/a)*(22/15))+ ((W + L)/v)*(15/22))
print("Yc = ",Yc)

VperS = (V * 2.25)/3600
print("VpS = ",VperS)
Cycle = math.ceil((2*3*X)/(X - VperS))
print("Cycle = ",Cycle)
LossTime = 2 * 3
Gsplit1 = (V1/V) * (Cycle -LossTime)
Gsplit2 = (V2/V) * (Cycle -LossTime)

Green1 = Gsplit1 - AmberTime + 3
Green2 = Gsplit2 -AmberTime + 3


Red1 = Cycle - (Green1 + AmberTime + Yc)
Red2 = Cycle - (Green2 + AmberTime + Yc)

print(Cycle)
print("Lane1")
print(Green1)
print(Red1)
print("Lane2")
print(Green2)
print(Red2)

