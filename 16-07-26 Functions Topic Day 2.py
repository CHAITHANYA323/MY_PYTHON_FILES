#YESTERDAY TASK
#BY USING MULTIPLE DEF KEYWORDS

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
                            1.add
                            2.sub
                            3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''


#KEYWORD AND POSTIONAL ARGUMENTS
#ARUGUMENT-1        
'''def Details (id,name,mailid):
    id=10
    name="pooja"
    mailid="ram@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

#ARUGUMENT-2
'''def Details (id,name,mailid):
       print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")#Headings nii print cheyyadaniki use chestham
Details(id=20,name="sai",mailid="sai@gmail.com")
Details(id=30,name="raju",mailid="raju@gmail.com")'''
        
#ARUGUMENT-3
'''def Details (id,name,mailid):
       print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(40,"srinu","srinu@gmail.com")#without passing the postional arguments (idhi order loo print avutundhi)'''

#ARUGUMENT-4
'''def Details (id,name,mailid):
       print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details("raju@gmail.com",70,"tej")'''#inorder keywords passing chesthe inorder lone print avtundhi

#ARUGUMENT-5
'''def Details (id,name,mailid):
       print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(mailid="raju@gmail.com",name="raju",id=30)'''#inorder loo positional arguments with keywords icchina avii order lone print avutundhi



#DEFAULT ARGUMENTS

#STEP-1
'''def Grocery(item,price):
    print('item is %s '%item)
    print('price is %.2f'%price)
Grocery ("rice",1500)

#STEP-2
def Grocery(item="sugar",price=100):
    print('item is %s '%item)
    print('price is %.2f'%price)
Grocery()

#STEP-3    
def Grocery(item,price=100):#non default arguments follows default arguments
    print('item is %s '%item)
    print('price is %.2f'%price)
Grocery("dhal")


#STEP-4   
def Grocery(item="sugar",price):#default arguments NOT follows non default arguments 
    print('item is %s '%item)
    print('price is %.2f'%price)
Grocery(1500)'''

#OUTPUT : ERROR -->#non default arguments follows default arguments
                   #default arguments --> item
                   #non default argument --> price=100 --> ilaga mention chesthe output vastundhi

                   #default arguments NOT follows non default arguments
                   #default arguments --> item="sugar"
                   #non default argument --> price --> ilaga mention chesthe output error vastundhi



#TASK

#cake_name,price,qty

#step-1
'''def bakery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %f"%price)
    print("qty is %f" %qty)
bakery("choclate",200,150) '''
    
#step-1
'''def bakery(cake_name="choclate cake",price=200,qty=150):
    print("cake_name is %s" %cake_name)
    print("price is %f"%price)
    print("qty is %f" %qty)
bakery()'''  
    
    
'''def bakery(cake_name,price=200,qty=150):
    print("cake_name is %s" %cake_name)
    print("price is %f"%price)
    print("qty is %f"%qty)
bakery("choclate")'''


'''def bakery(cake_name="choclate",price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %f"%price)
    print("qty is %f" %qty)
bakery(200,150)''' #OUTPUT: ERROR



#STAR ARUGMENTS

# *arguments (* is used to unpack the elements)

#LIST
a=[10,20,30,40,50]
print(a)
print(*a)

#TUPLE
b=(5,6,7,8,9,10)
print(b)
print(*b)

#SET
c={6,7,8,9,10}
print(c)
print(*c)

#DICT
print={"name":"chaithu","year":2026,"month":7}
print(d)

#STRING
a="codegnan"
print(a)
print(*a)

a,b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(c) #-->OUTPUT: ERROR

#BY USING *STAR ARGUMENT WE CAN DO IT

#FOR EXAMPLE:

a,b,*c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)

a,*b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(*b)
print(c)

*a,b,c=2,3,4,5,6,7,8,9,10,11
print(*a)
print(b)
print(c)

*a,b,*c=2,3,4,5,6,7,8,9,10,11
print(*a)
print(b)
print(c) #-->OUTPUT:ERROR

a,b,c="codegnan"
print(a)
print(b)
print(c) #-->OUTPUT: ERROR


a,b,c="cod"
print(a)
print(b)
print(c)


#BY USING *STAR ARGUMENT
a,b,*c="codegnan"
print(a)
print(b)
print(c)




