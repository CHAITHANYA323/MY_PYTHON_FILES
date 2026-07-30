#EXCEPTION HANDLING

#In exception handling we have four blocks:
'''1.try
2.except
3.else
4.finally'''

'''while True:
    try:
        a=int(input("a value:")
        b=int(input("a value:")
        c=a//b
        print(c)

    except:
        print("expection is raised")
    else:
        print("no expections")
    finally:
        print("programs ends")'''
        

#REGEX (or) REGULAR EXPRESSIONS
'''a="codegnan is in vja"
print(a)

a="codegnan\nis \tis \nvja"
print(a)

#rsting--> it is not changable when we exec the prgm (it is only work in regex) 
a=r"codegnan\nis \tis \nvja"
print(a)'''

#IN REGEX WE HAVE FOUR METHODS:
'''1.compile()
2.search()
3.findall()
4.split()
5.sub()'''

#SEQUENCE CHARACTERS
'''1.\w--> it matches alphanumeric
2.\W-->it matches non-alhanumeric
3.\d-->it matches any digit
4.\D-->it matches non-digit
5.\s-->it represents white spaces
6.\S--> it represents non-white spaces'''


#1.compile()
'''import re
a="mat map cap cup money  cash cat dog mug donkey  maths"
b=re.compile(r"m\w\w\w\w\w")
print(b)'''

#2.search()
'''import re
a="mat map cap cup money  cash cat dog mug donkey  maths"
b=re.compile(r"m\w\w\w\w\w")
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#3.findall()
'''d=re.findall(r"m\w+",a)'''

#4.split()
'''e=re.split(r"m",a)
print(e)

f=re.split(r"\s",a)

f=re.split(r"\S",a)'''


#5.sub()
'''g=re.sub(r"m',"a",a)
print(g)'''

#\d & \D 
c="year 2026 month 7 date 30"
d=re.findall(r"\d",c)
print(d)

c="year 2026 month 7 date 30"
d=re.findall(r"\d+",c)
print(d)

c="year 2026 month 7 date 30"
d=re.findall(r"\D+",c)
print(d)

         
         


