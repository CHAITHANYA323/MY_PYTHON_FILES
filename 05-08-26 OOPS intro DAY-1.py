#OOPS
#SYNTAX

'''class classname(): #class creation
    #attributes
    name="chaithu"
    age="19"
    place="viz"
    def functionname(method_name):-->function creation & method 
        print(statements.......)
object=classname()-->object creation
object.functionname()'''

#CLASS DECLARATION
'''class details():
     name="chaithu"
     age="19"
     place="viz"
     def display(self):
         print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''


#OBJECT INSTANTIATION
class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("chaithu",18,"viz")
a.display()
b=details()
print(dir(a))
b.data("vishnu",21,"vij")
b.display()
c=details()
print(dir(a))
c.data("sai",19,"vizag")
c.display()
    
    
