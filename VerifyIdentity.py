from RPi import GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def open_lock():
    GPIO.setup(4, GPIO.IN)

def close_lock():
    GPIO.setup(4, GPIO.OUT)

FAILEDATTEMPTS = 0

while True:
    if FAILEDATTEMPTS == 3:
        print("Too many failed attempts to get in safe.")
        break

    # Wait for user to press enter to take photo
    input("Press enter to attempt access to safe...") 

    # Take the person's picture, save the location of the image
    imgLoc = subprocess.run(['./take_photo.sh'], capture_output=True).stdout.decode('utf-8') 
    
    # Send image to webserver, check whether or not they have permission to open safe
    permission = subprocess.run(['./send_photo.sh', imgLoc], capture_output=True).stdout.decode('utf-8')
    
    if permission == "Valid\n":
        FAILEDATTEMPTS = 0
        open_lock() # Open the lock
        sleep(7) # You have 7 seconds to open the safe before the lock is set again
        close_lock() # Close the lock
    else:
        FAILEDATTEMPTS+=1
        print("Permission denied, please try again.")
