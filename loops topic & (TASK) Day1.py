#loops
#for loops,while,,range,break,continue,pass

'''#for loop()
a=[10,20,30,40,50]
for i in a:
    print(i)
#list
a=[10,20,30,40,50,60]
for i in a:
    print(a)

    
a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))
    
a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))

#Tuple
a=(4,5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))

a={4,5,6,7,8,9}
for i in a:
    print(i)
print(type(a))
print(type(i))

d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
for i in d.keys():
    print(i)
    print(type(d))
    print(type(i))

for i in d.values():
    print(i)
    print(type(d))
    print(type(i))


a="codegnan"
for i in a:
    print(i)

a=[3.4,5.6]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=["python","java","html","css"]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[5+9j,2+10j]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[True,False]
for i in a:
    print(i)
print(type(a))
print(type(i))'''


#Task-1 by using for loop and append method()


'''a=["apple","banana","mango"]
for i in fruits:
    print(i.upper(),end=" ")


#solutions
a=["apple","banana","mango"]
b=[]
for i in a:
    b.append(i.upper())
print(b)

#by converting into string method
 b=str(a)
 print(b.upper())'''

#Task-2 by using extend method

'''a=[10,20,30,40,50,"code"]
a.extend("code")
print(a)'''
 
#Task-3 by using insert method 
#input a=[2,3,5,6,7]
#output [2,3,4,5,6,7]

a=[2,3,5,6,7]
a.insert(2,4)
print(a)


#Task-4 by (using list to tuple and tuple to list)
#input b=(5,6,7,8,9,10)
#output =(5,6,7,8,9)

b=(5,6,7,8,9,10)
c=list(b)
print(c)
c.remove(10)
print(c)
d=tuple(c)
print(d)

#Task-5 by using sort()
#e=[7,9,0,1,4,9,3,20]
#ouptut=[0,1,2,3,4,7,9,9,20]

e=[7,9,0,1,4,9,3,20]
e.sort()
print(e)
    
