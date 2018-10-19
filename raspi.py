import mysql.connector
import RPi.GPIO as GPIO
from time import sleep


Motor1A = 24
Motor1B = 23
Motor1E = 25
f=0

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
while(1):
        try:
                con = mysql.connector.connect(host='localhost',database='mydb',user='jerry',password='2308')
                cursor = con.cursor()
                sql = "SELECT * FROM status_table "
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                for row in results:
                        id = row[0]
                        status = row[1]
                        setup()
                        if (status=="booked" and f==0):
                                GPIO.output(Motor1A,GPIO.LOW)
                                GPIO.output(Motor1B,GPIO.HIGH)
                                GPIO.output(Motor1E,GPIO.HIGH)
                                sleep(0.0145)
                                GPIO.output(Motor1E,GPIO.LOW)
                                print("up")
                                print(id, status)
                                f=1
                        elif (status=="parked" and f==1):
                                GPIO.output(Motor1A,GPIO.HIGH)
                                GPIO.output(Motor1B,GPIO.LOW)
                                GPIO.output(Motor1E,GPIO.HIGH)
                                sleep(0.0255)
                                GPIO.output(Motor1E,GPIO.LOW)
                                print("down")
                                print(id, status)
                                f=0
                        #else:
                                #GPIO.output(Motor1A,GPIO.LOW)
                                #GPIO.output(Motor1B,GPIO.HIGH)
                                #GPIO.output(Motor1E,GPIO.HIGH)
                                #print("down-make free")
        except:
                print ("Error: unable to fecth data")
                




# disconnect from server
con.close()
