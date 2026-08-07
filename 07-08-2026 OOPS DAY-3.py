#METHOD OVERLOADING

'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is ",a+b+c)
        elif a!=None and b!=None:
            print("the product  is ",a*b)
        else:
            print("program ends......")
x=new()
x.sum() 
x.sum(2,3,4)
x.sum(5,6)'''

#TASK
'''class new():
    def sum(self,a=2,b=3,c=4):
        if a!=2 and b!=4 and c!=4:
            print("the sum is ",a+b+c)
        elif a!=4 and b!=5:
            print("the product  is ",a*b)
        else:
            print("program ends......")
x=new()
x.sum()'''

#METHOD OVERRIDING

'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def spring(self):
        print("dog can barks")'''
        

#This is method overriding
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
        
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#Task
'''class vehicle():
    def ride(self):
        print("vehicles move on the road")
class herobike():
    def ride(self):
        print("hero can get less price")
a=vehicle()
b=herobike()
a.ride()
b.ride()



class car():
    def vehicle(self):
        print("THAR")
class bike():
    def vehicle(self):
        print("HERO")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''



#INHERITANCE
#Inheritance we have FIVE Types:
'''1.single Inheritance
2.multiple Inheritance
3.multi-level Inheritance
4.Hybrid Inheritance
5.Herchical Inheritance'''

#1.Single Inheritance

'''class RBI():#parent class
     cash=100000
     def available_cash(cls):
            print("available_cash is",cls.cash)
            #print("available_cash is",RBI.cash)
class SBI(RBI): #child class-1
    pass
class HDFC(RBI): #child class-2
    cash=50000
def new_cash(cls):
    print("new_cash is",cls.cash+cls.cash)
   #print("new_cash is",RBI.cash)
a=HDFC() 
a.available_cash()
a.new_cash()'''

    
#2.multiple Inheritance()

#Task
class father():
    weight=65
    def weight_father(self):
          print("Weight of father is",self.weight)
class mother():
     height=5.5
     def height_mother(self):
         print("Height of mother is",self.height)
class kid(father,mother):
     DOB=26
     def Dob_kid(self):
         print("DOB of kid is",self.DOB)          
b=kid()
b.weight_father()
b.height_mother()
b.Dob_kid()

#Mentor Explained code
#Without using inheritance concept
'''class father():
    def weight():
        print("60kgs")
class mother():
    def height():
        print("5.5 inches")
class kid(father,mother):
    def Dob:
         print("just born......")        
a=father()
a.weight()
b=mother()
b.height()
c=kid()
c.Dob()'''


#With using inheritance concept
'''class father():
    def weight():
        print("60kgs")
class mother():
    def height():
        print("5.5 inches")
class kid(father,mother):
    def Dob:
         print("just born......")        

c=kid()
c.father()
c.mother()
c.Dob()'''



    





