from gpiozero import OutputDevice, Button
import subprocess
from time import sleep

button = Button(2)
lock = OutputDevice("BOARD7", active_high=True, inital_value=False, pin_factory=none)

while True:
    # Wait for user to press button to take photo
    button.wait_for_press()

    # Take the person's picture, save the location of the image
    imgLoc = subprocess.run(['./take_photo.sh', '1']) 
    
    # Send image to webserver, check whether or not they have permission to open safe
    permission = subprocess.run(['./send_photo.sh', imgLoc], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    if permission == "Valid\n":
        lock.on() # Open the lock
        sleep(10) # You have 10 seconds to open the safe before the lock is set again
        lock.off() # Close the lock
    else:
        # Future work, potentially email picture of person who tried to open safe
        print("Permission denied")





