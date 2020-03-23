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



now = time.time()
sec = int(now % 60)


t = 1
a = 15
v = 30
L = 20

flow1 = randint(0,10)*80
flow2 = randint(0,10)*80

S1 = randint(40,100)
S2 = randint(40,100)


clctime = math.floor(t + ((0.5)*(v/a)*(22/15))+ ((W + L)/v)*(15/22))

AmberTime = 3
LossTime = 2 * clctime

y1 = flow1/S1
y2 = flow2/S2

Y = y1 + y2

Cycle = (1.5*L + 5)/(1-Y)

G1 = ((y1/Y)*(Cycle - L))
G2 = ((y2/Y)*(Cycle - L))

R1 = Cycle - (G1 + L)
R2 = Cycle - (G1 + L)

allread = Cycle - (G1 + R1)

# if key == 6 and c == 0:
# 	c == 10
# 	count = 0
# 	pre = sec
# 	if pre == 59:
# 		pre = 0
# 	print(sec)
# 	cv2.imwrite(filename='car.jpg', img=frame)
# 	img_new = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)
# 	img_ = cv2.imread('car.jpg', cv2.IMREAD_ANYCOLOR)
# 	image = cv2.imread("car.jpg")
# 	thread.start_new_thread( cc, ("image",2 , ) )
# else:
# 	c = 0
