#Task-1
#swapping of two variables

#without using temp varaible
'''a=int(input("enter value a"))
b=int(input("enter value b"))
a=a+b
b=a-b
a=a-b
print("after swapping the result is ")'''

#using  temp variable
'''a=int(input("enter value a"))
b=int(input("enter value b"))
temp=a
a=b
b=temp
print("after swapping the result is ")
print("a=",a)
print("b=",b)'''

#without using temp variable 
'''a=int(input("enter value a"))
b=int(input("enter value b"))
a=a*b
b=a//b
a=a//b
print("after swapping the result is ")
print("a=",a)
print("b=",b)'''

#using python tuple
'''a=int(input("enter value a"))
b=int(input("enter value b"))
a,b=b,a
print("after swapping the result is ")
print("a=",a)
print("b=",b)'''

#fourth method by using number formatting
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%a b=%d "%(a,b))'''


'''a=float(input("enter value a"))
b=float(input("enter value b"))
a=a+b
b=a-b
a=a-b
print("after swapping a=%f b=%f "%(a,b))'''


'''a=(input("data1:"))
b=(input("data2:"))
temp=a
a=b
b=temp
print("after swapping a=%s b=%s "%(a,b))'''


a=str(input("data1:"))
b=str(input("data2:"))
temp=a
a=b
b=temp
print("after swapping a=%s b=%s "%(a,b))



