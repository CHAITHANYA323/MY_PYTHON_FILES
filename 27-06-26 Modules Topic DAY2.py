#MATH MODULE--> is used to calculate the math calculations

'''import math
print(math.pi)
print(math.pi*3)
print(math.pi*3)
print(math.sqrt((2))
print(math.pow(2,2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))      
print(math.sin(30))
print(math.ceil(4.9))
print(math.floor(6.9))

#From key---> it is used to get more packages at time 
form math import pi,sqrt,log,tan,cos
print(pi)
print(sqrt(2))
print(tan(45))
print(log(20))
print(cos(60))      
print(math.cos(60))-->#ERROR


#SYSTEM MODULE--> SYS module -it is used to check the system version,python version,system path or location it means where your file is exactly located.

import sys
print(sys.path)      
print(sys.version)'''


#OPERATING SYSTEM MODULE--> OS MODULE
      
'''import os
print(os.path)
print(os.getcwd)
print(os.listdir())
print(os.chdir("C:\\Users\\Lap12NOC\\Desktop\\pythonfiles"))      
print(os.listdir())
print(os.mkdir("july27"))'''


#RANDOM MODULE DEFINTION--> RANDOM MODULE IS USED TO GENENATE THE RANDOM NUMBERS IN PYTHON RANDING FUNCTION IS USED AND THIS FUCNTION IS DEFINING RANDOM MODULING.

#In the random module we have three variants:
'''1.Sample of Range
2.randiant
3.choice

#Sample of Range
import random
a=random.sample(range(20,40),10)
print(a)

#Randiant
import random
a=random.randiant(20,50)
print(a)

#Choice
import random
a=[10,30,50,70,90]
b=random.choice(a)
print(b)'''



#Dice Code
'''while True:
    dice = int(input("Enter the roll of Dice (1-6): "))

    if 1 <= dice <= 6:
        print("You rolled:", dice)
    else:
        print("Invalid dice value!")
    print("\nOptions")
    print("1. Yes")
    print("2. No")

    choice = int(input("Do you want to roll again? Enter your choice: "))

    if choice == 1:
        continue
    elif choice == 2:
        print("Program Stopped")
        break
    else:
        print("Invalid Choice! Program Stopped")
        break'''
    
    
    
