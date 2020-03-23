import threading
import time
import serial
import mysql.connector
from mysql.connector import Error



class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      ReadWriteSerial(self.name):
      print ("Exiting " + self.name)
