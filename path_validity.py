#Calling os.path.exists(path) will return True if the file or folder referred
#to in the argument exists and will return False if it does not exist.
#Calling os.path.isfile(path) will return True if the path argument exists
#and is a file and will return False otherwise.
#Calling os.path.isdir(path) will return True if the path argument exists
#and is a folder and will return False otherwise.
import os 

print(os.path.exists('/home/daniel/Documents/SNIPS'))

print(os.path.isfile('/home/daniel/Documents/SNIPS'))

print(os.path.isdir('/home/daniel/Documents/SNIPS'))

#to check whether a flash disk or dvd is plugged into the computer
print(os.path.exists('/D://'))