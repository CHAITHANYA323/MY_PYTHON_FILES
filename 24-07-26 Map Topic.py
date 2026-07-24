#MAP()

#MAP Def: Each Object from a collection and forms a new collection

'''a=[2,36,7,8,10,12,14,16,20]
b=[1,3,5,7,9,10,13,15,17,21]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

#RUN_TIME Input Formats
#different types of run_time inputs

#1.Normal run_time input
a=input("data1")
b=input("data2")
print(a+b)'''

#By using split method
'''a,b=input("enter the data").split(",")
print(a+b)

#List compreshension
a,b=[x for x in input ("data").split(",")]
print(a+b)


#Generators
a,b=(x for x in input ("data").split(","))
print(a+b)


#MAP
a,b=map(str,input("enter the values ").split(","))
print(a+b)'''

#BY USING (Int Data type)
'''a=int(input("data1"))
b=int(input("data2"))
print(a+b)


a,b=[int(x) for x in input ("data").split(",")]
print(a+b)


a,b=(int(x) for x in input ("data").split(",")
print(a+b)


a,b=int(input("enter the data").split(","))
print(a+b) #ERROR (split method doesnot work by using int datatype)

a,b=map(int,input("enter the values ").split(",")))
print(a+b)'''
     

#In map() Function we can pass List,Tuple,Set by using Run_Time input  
'''a=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))

a=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))     

a=set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

a=dict(map(int,input("enter the values").split(",")))
print(a)
print(type(a)) #ERROR

#In DICT map fucntion doesnot work
a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)



#TASK

#BMI mini project

while True:
    height=float(input("enter the height"))
    weight=float(input("enter the weight"))
    bmi=weight/(height)**2
    if bmi<=18.5:
        print("under weight")
    elif bmi>18.5 and bmi<=24.5:
        print("healthy weight")
    elif bmi>24.5 and bmi<=29.5:
        print("over weight")
    elif bmi>30:
        print("obesity")


        



