#Object intialization

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("chaithu",18,"vizag")
print(dir(a))
a.display()'''

#Task (BY using user_input())
#METHOD-1
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(int(input("name")),int(input("Age")),input("place"))
print(dir(a))
a.display()'''


#METHOD-2
'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=input("age")
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''
    



#DIfference between _ and __

class Employee():
    def __init__(self):
        self.name="sai"
        self._emailid="sai@gmail.com"
        self.__salary=50000
a=Employee()
print(dir(a))
print(a.name)
print(a._emailid)
print(a.__salary) #Error
print(a.__employee__salary)



class Employee1():
    def __init__(self):
        self.name="charan"
        self._mailid="charan@gmail.com"
        self.__salary=50000#private variable

class Employee2():
    def __init__(self):        
        self.name="chaithu"
        self._mailid="chaithu@gmail.com"
        self.__salary=30000#private variable 
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary) #Error
print(a.__Employee1__salary)

b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary) #Error
print(b._Employee2__salary)



#

#POLYMORPHISM
#1.OPERATOR OVERLOADING
#BY USING VARIABLES
a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(3))
print(a.__sub__(1))
print(a.__mul__(6))
print(a.__div__(2))
print(a.__pow__(2))
print(a.__eq__(2))
print(a.__le__(5))
print(a.__ge__(10))
print(a.__ge__(1))

#BY USING LIST

#method--getitem--> accesing the item
a=[2,3,4,5,6];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(4))

a="code";b="gnan"
print(a.__add__(b))
a="python";b="gnan"
print(a.__add__("+b"))
print("chaithu".__add__("" "+ka").title())


#operator overriding
class A():
    def __init__(self,a):
        self.a=a
    def__add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
#x=A(4)
#y=B(5)
x=4
y=5
print(x+y)




        
