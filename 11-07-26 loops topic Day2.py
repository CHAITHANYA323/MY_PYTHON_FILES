#while loop()
'''a=10
while a>1:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1

a=10
while a>=1:
    print(a)
    a=a-1

a=10
while a>1:
    a=a-1
    print(a)

a=20
while a>5:
    a=a-1
print(a)

a=30
while a>2:
    print(a)
    a+=1
    
a=30
while a>2:
    print(a)
    a-=1

a=5
while a<25:
    print(a)
    a+=1'''


#voting

'''while True:
    age=int(input("enter the value")
    if age>=18:
            print("eligible for vote")
    else:
        print("not eligible for vote")'''

#range()

#start-stop-step

'''for i in range(10):
    print(i)

for i in range(5,15):
    print(i)


for i in range(30,45):
    print(i,end=",")'''
    
        
#Task-1

#output=2,4,6,8,20,12,14,16,18
        
'''for i in range(2,20,2):
    print(i)



#output=5,10,15,20,25,30,35,40,45

for i in range(5,50,5):
            print(i)

#output=0,3,6,9,12,15,18,21,24,27

for i in range (3,30,3):
            print(i)'''

#Grades
while True:
    a=int(input("enter the marks"))
        if a in range(91,101):
                   print("Grade A")
        elif a in range(81,91):
                   print("Grade b")
        elif a in range(71,81):
                   print("Grade c")
        elif a in range(50,71):
                   print("Grade D")
        else:
                   print"'fail")

       
#Break
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break
    
                   
       
a=30
while a>2:
    a=a-1
    if a==20:
        break
    print(a)
    


for i in range (40,65):
    if i==55:
        break
    print(i)


a="python"
if a=="h":
    break
print(a) #error



a="python"
for i in a:
    if i=="h":
        break
    print(i)

    

#continue

a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue #output : print the 15 to 3
    
a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue

    
for i in range (18):
    if i==14:
        continue
    print(i)
    
a="python"
for i in a:
    if i=="t":
        continue
    print(i)


#pass

a=12
while a>4:
    print(a)
    a=a-1
    if a==10:
        pass

for i in range(25)
      if a==10:
          pass
      print(i)
    
    
