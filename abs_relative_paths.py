import os

print(os.path.abspath('.'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

#getting file sizes
print(os.path.getsize('/home/daniel/Documents/P LEARN'))
print(os.listdir('/home/daniel/Documents/P LEARN'))

#to find the total size of all files in this directory
totalsize=0
for x in os.listdir('/home/daniel/Documents/P LEARN'):
    totalsize=totalsize+os.path.getsize(os.path.join('/home/daniel/Documents/P LEARN',x))

print(totalsize)