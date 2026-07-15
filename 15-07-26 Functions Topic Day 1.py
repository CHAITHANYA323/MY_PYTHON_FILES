#FUNCTIONS

#Basic Program

'''a=10
b=20
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is",a*b)


a=100
b=200
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is",a*b)


a=1000
b=2000
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is",a*b)'''


#syntax: def_keyword user_defined_name (aruguments or parameters)--> calling function:
            
                #block  of code

         #called function

'''def calculate (a,b):
    print("the sum is ",a+b)
    print("the diff is ",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''



'''def calculate (a,b):
    print("the power is ",a**b)
    print("the modules is ",a%b)
    print("the Integer Division is",a//b)
calculate(10,20)
calculate(2,4)
calculate(5,8)'''


#functions  by using runtime_intput

'''def add():
    a=int(input("a value")
    b=int(input("a value")      
    print(a+b)
add()'''
          

#function by using whileloop (continue iteration)


'''def add():
    a=int(input("a value")
    b=int(input("a value")      
    print(a+b)
add()'''         
          

#By using recursive function without using while loop (continue iteration)

'''def add():
    a=int(input("a value")
    b=int(input("a value")      
    print(a+b)
    add() #RECURSIVE FUNCTION      
add()'''


#usecase by using functions

'''def fullname() :
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''   
    
          

#DIFFERENCE B/W PRINT AND RETURN

#print

'''def mul (a,b):
    print(a*b)
mul(4,6)

def mul (a,b):
    print(a,b)
print(mul(1,3))''' #CALLBACK FUNCTION


#PRINT V/S RETURN

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
#or
    print(c,d,e)
cal(2,3)'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
#or
    return c,d,e
print(cal(7,3))'''
    

#Task-1

#SPLITBILL()
'''def splitbill():
   a=int(input("enter the total number")
   b=int(input("enter the Amount")
   print("per head bill is ",b//a)#integer divison is used to split bill      
splitbill()'''


#Task-2 splitbill by using f string and Dot format method
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()'''


'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    print("per head bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
splitbill()'''


#TASK 

def maths():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))

    print("""
Options:
1. Add
2. Sub
3. Mul
""")

    choice = int(input("Enter your option: "))

    if choice == 1:
        print("Addition is =", a + b)

    elif choice == 2:
        print("Subtraction is =", a - b)

    elif choice == 3:
        print("Multiplication is =", a * b)

    else:
        print("Invalid option")

maths()




    
        

