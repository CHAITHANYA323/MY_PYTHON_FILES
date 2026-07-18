#GLOBAL AND LOCAL VARIABLES (OR) SCOPE OF THE VARAIBLES

#First case of Global Variables
'''a=3
def check1():
    print("inside value is",a)
check()
print("outside value is",a)


#Second case of Global Varaible
a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)


#Third case of Both global and local varibles
a=2 #GLOBAL VARIABLES
b=9
def check3():
    a=7
    print("inside value is ",a)
    a=10
    print("updared value is",a+5)
    b=14 #LOCAL VARIABLE
    b=b+a
    print("value of b is ,b)
check()
print("a value is",a)
print("b value is",b)          
          
#FOURTH CASE OR FINAL CASE
#USAGE OF GLOBAL KEYWORD

#By using to individual global variables
a=5
def final():
    global a
    print("inside value is",a)
    a=10
    print("updated value is",a)
    global b
    b=15
    b=b+a
    print("value of b is ",b)
final()
print("a value is",a)
print("b value is",b)

#By using to single global variables 
a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value of b is ",b)
final()
print("a value is",a)
print("b value is",b)'''



#ATTENDANCE TRACKING REPORT

'''students=int(input("enter the students stength:"))
p=0
a=0
for i in range(1,students+1):
    attendance=input (f"student{i}(p/a)")
    if attendance=="p":
        p+=1
    elif attendance=="a":
        a+=1
              
print("---ATTENDANCE REPORT---")
print("total students",students)
print("total presenties",p)
print("total absenties",a)'''






    
