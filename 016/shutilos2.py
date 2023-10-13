import os

import shutil
print(os.getcwd())
print(os.path.isfile("test.py"))
print(os.path.isfile("12"))
print(os.path.isdir("12"))

#shutil.copy("sourcefile","destinationfile") rename , copy 
#shutil.copy("test.txt","test5.txt")
#shutil.move("sourcefile","destinationfile") rename va move 
#shutil.move("test.txt","12\\test555.txt")
#shutil.rmtree remove tree
shutil.rmtree("12")
