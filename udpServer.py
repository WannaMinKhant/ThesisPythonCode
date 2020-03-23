#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:36:38 2020

@author: wunnaminkhant
"""

import mysql.connector as mariadb
from mysql.connector import errorcode
import socket
import sys
from random import randint




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