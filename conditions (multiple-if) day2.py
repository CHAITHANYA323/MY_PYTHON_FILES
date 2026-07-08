#multiple-if conditions
#By using comparsion operators
a=20
b=40
if a<b:
    print("true")
if a>b:
    print("true")
if b>a:
    print("true")
if a==b:
     print("true")
if a!=b:
    print("true")


#Difference between multiple if and multiple elif conditions
    
if a<b:
    print("true")
elif a>b:
    print("true")
elif b>a:
    print("true")
elif a==b:
     print("true")
elif a!=b:
    print("true")

else:
    print("false")


 #By using  logical operators multiple-if conditions
    
if  a>b and b>a:
    print("true")
if a<b and b<a:
    print("true")
if a>b or b>a:
    print("true")
if a<b or b<a:
    print("true")
    
    
#By using  identify  operators multiple-if conditions
a=15
if type(a) is float:
    print("It is float")
if type(a) is str:
    print("it is string")
if type(a) is int:
    print("it is int")

#By using  membersship operators multiple-if conditions
a=1,2,3,4,5,6
if 3 in a:
    print("it is true")
if 10 in a:
    print("it is true")
if 5 in a:
    print("it is true")
if 10 not in a:
   print("it is true")
if 5 not in a:
    print("it is true")
    
    
    

    
    

    
    
    
