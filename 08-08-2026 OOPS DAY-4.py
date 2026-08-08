#MULTI-LEVEL INHERITANCE-->one class inherits from another class,and a third class inherits from the second class

'''class grandparent():
    def land(self):
        print("2 acres")
class parent(grandparent):
    def house(self):
        print("100sqt")
class child(parent):
    def car(self):
        print("THAR")        
a=child()
a.land()
a.house()
a.car()'''


#HIERARCHICAL INHERITANCE--> single parent and multiple child classes

'''class employee(): #parent class
    def company(cls):
        print("ensoft PVT.Ltd")
class trainer(employee):
    def Teaching(cls):
        print("Industry skills")
class student(employee):
    def study(cls):
        print("Real time work experience")        
a=trainer()
a.company()
a.Teaching()
b=student()
b.comapany()
b.study()'''


#HYBRID INHERITANCE--> combination of both multi-level inhertiance & hierachical inheritance

class person():
    def details(self):
        print("chaithu",28,"male")
class trainer(person):
    def teach(self):
        print("Trianer the course to the students")
class student(person):
    def study(self):
        print("student improve there techincal skills from the trainer")
class programmanger(trainer,student):
    def manager(self):
        print("program management monitor the trainer & students")
a=programmanger()
a.details()
a.teach()
a.study()
a.manager()



#super():built_function--> is used to access the parent class methods and constructor from the child class
#without super 
class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("child constructor")
a=child("chaithu",19)
print(a.name)
print(a.age)


class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child():
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("childconstructor")
a=child("chaithu",19)
print(a.name)
print(a.age)        

    
