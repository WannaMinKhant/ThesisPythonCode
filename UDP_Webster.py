import mysql.connector as mariadb
from mysql.connector import errorcode
import socket
import sys
from random import randint
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("Width", help="Enter lane width at the junction",
                    type=int)
arg = parser.parse_args()
W = arg.Width


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.100', 5000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

check = 1
lane1 = 0
lane2 = 0

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    ip, _ = address
    #print >>sys.stderr, ip
    
    if ip == '192.168.0.101':
        lane1 = 1
        adr1 = address
        print >>sys.stderr, '\nlane1'
    elif ip == '192.168.0.102':
        lane2 = 1
        adr2 = address
        print >>sys.stderr, '\nlane2'
        
    if lane1 == 1 and lane2 == 1:
        flow = randint(10,30)
        p1 = flow + 5
        p2 = flow
        sent = sock.sendto('%s:%s' % (p1, p2), adr1)
        sent = sock.sendto('%s:%s' % (p2 , p1), adr2)
        
        print >>sys.stderr, 'sent %s bytes back to %s' % (p1, adr1)
        print >>sys.stderr, 'sent %s bytes back to %s' % (p2, adr2)
        lane1 = 0
        lane2 = 0
        print >>sys.stderr, '\nCycle update'
        
def WebsterMethod(flow1,flow2,S1,S2):
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
        

def SelectDB():
    flow1 = 0
    flow2 = 0
    sat1 = 0
    sat2 = 0
    delay = 0
    img = "gaung.jpg"
    global count
    
    try:
        connection = mariadb.connect(host='localhost',
                database='traffic', user='minkhant', password='root')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print ('Connected to MySQL Server version ', db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            mySql_insert_query = \
                """SELECT * FROM lane1 """

            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            
            results = cursor.fetchall()
            count = 0
            for row in results:
                count += 1
                flow1 = row[2]
                flow2 = row[3]
                sat1 = row[4]
                sat2 = row[5]
                delay = row[1]
                
            WebsterMethod(flow1,flow2,sat1,sat2)

    except IOError as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print ('MySQL connection is closed')
            

    
