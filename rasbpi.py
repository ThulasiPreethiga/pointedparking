import mysql.connector
#import RPi.GPIO as GPIO
from time import sleep

con = mysql.connector.connect(host='localhost',database='parking',user='root',password='')
Motor1A = 24
Motor1B = 23
Motor1E = 25

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
cursor = con.cursor()
sql = "SELECT * FROM status_table "
try:
        #Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      status = row[1]
      #setup()
      if status=="booked":
              #GPIO.output(Motor1A,GPIO.HIGH)
	      #GPIO.output(Motor1B,GPIO.LOW)
	      #GPIO.output(Motor1E,GPIO.HIGH)
              print("up")
      # Now print fetched result
      elif status=="parked":
              #GPIO.output(Motor1A,GPIO.LOW)
              #GPIO.output(Motor1B,GPIO.HIGH)
              #GPIO.output(Motor1E,GPIO.HIGH)
              print("down")
      else:
              #GPIO.output(Motor1A,GPIO.LOW)
	      #GPIO.output(Motor1B,GPIO.HIGH)
	      #GPIO.output(Motor1E,GPIO.HIGH)
              print("down-make free")
      print (id, status)
except:
   print ("Error: unable to fecth data")




# disconnect from server
con.close()
