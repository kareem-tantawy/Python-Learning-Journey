# --------------------------------
# -- File Handling => Read File --
# --------------------------------

import os  # => stands for operating system

print(os.getcwd()) # => prints the current working directory

print(os.path.abspath(__file__)) # => prints thee directory for the current file

os.chdir(os.path.dirname(__file__)) # => changes the cwd to the file directory


myFile = open(r"e:\mohamed\plain.txt", "r")

print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read())
print(myFile.read(5))

print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

    print(line)

    if line.startswith("07"):

        break

# Close The File

myFile.close()
