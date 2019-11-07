import subprocess
from time import sleep

# Take the person's picture, save the location of the image
# imgLoc = subprocess.run(['./take_photo.sh', '1']) COMMENT UNTIL CAMERA WORKS
imgLoc = 'Pictures/dog1.jpeg'

# Send image to webserver, check whether or not they have permission to open safe
permission = subprocess.run(['./send_photo.sh', imgLoc], stdout=subprocess.PIPE).stdout.decode('utf-8')

if permission == "Valid\n":
    subprocess.run(['python3', 'Safe.py', 'unlock'])
    sleep(10) # You have 10 seconds to open the safe before the lock is set again
    subprocess.run(['python3', 'Safe.py', 'lock'])
else:
    # Future work, potentially email picture of person who tried to open safe
    print("Permission denied")


