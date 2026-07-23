#MARKS ANALYSIS REPORT

'''students=int(input("enter the no.of students"))
marks=[]
for i in range (1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".......marks analysis report.......")
print("total  students",students)
print("highest marks",max(marks))
print("lowesr marks",min(marks))
print("total marks",sum(marks))
print("Average",sum(marks)/students)'''

#TASK

#write a function to calculate 2*x+5 where x=5

'''def calculate(x):
    print (2*x+5)
calculate(5)


def calculate():
    x=int(input())
    print(2*x+5)
calculate()

#ANNONYMOUS FUNCTIONS
#SYNTAX
#a=lamba arg:expr
#lamba-->keyword
#arg--> variable
#expr-->expression given in the question

a=lamba x:2*x+5
print(a(5))


#BY USING RUN TIME INPUT
a=int(input())
b=lamba x:2*x+5
print(b(a))

#TASK-1

#Take 2 arguments and multiply it

a=lamba a,b:a*b
print(a(3,5))

a=int(input())
b=int(input())
c=lamba a,b:a*b
print(c(a,b))

#TASK-2

#a="codegnan"
#CODEGNAN


b=lamba a:a.upper()
print(b(a))



a=lamba a:a.upper()
print(a("codegnan"))


a=int(input())
b=lamba a:"codegnan"
print(b(a).upper())
    


#TASK-3
b="python course"
#Python Course
c=lamba a:a.title()
print(c(b)),,,


#firstname+lastname=fullname
fname=input("first name")
lname=input("last name")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''


fname,lname=[x for x in input("enter the names").split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))


#FILTER() METHOD TOPIC

#TASK
a=[10,20,23,25,67,45,80,90,97,85,100]
#print all even numbers





