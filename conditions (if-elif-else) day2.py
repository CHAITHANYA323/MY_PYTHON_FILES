#if-elif-else conditions by using comparision operators
a=8
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")

#multiple elif-else
a=8
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("both are not equal")
elif a==b:
    print("both are equal")    
else:
    print("true")    

#Task
#By using logical operators   
a=8
b=10
if a>b and b<a:
    print("less")
elif b>a and a>b:
    print("greater")
elif a!=b or b==a:
    print("both are not equal")
elif b<=a or b>=a:
    print("both are equal")
elif  not b<=a:
    print("both are equal")      
else:
    print("true")


#By using membership operators    
a=1,2,3,4,5,6,7
if 2 in a:
    print("less")
elif  10 in a:
    print("greater")
elif 9 not in a:
    print("both are not equal")
elif 10 not in a:
    print("both are equal")    
else:
    print("true")


#By using identify operators   
a=10
if type (a) is float:
    print("it is float")
elif type(a) id str:
    print("it is string")
elif type(a) is not int:
    print("it is not int")
elif type(a) is int :
    print("it is integer")    
else:
    print("it is not integer")


    
    


    
    
