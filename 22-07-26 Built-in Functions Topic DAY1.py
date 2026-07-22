#BUILT FUNCTIONS

#print(dir())  --> ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

'''print(dir("__builtins__"))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
 '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
 'upper', 'zfill']'''


'''a="codegnan"
print(a)
print(list(a))--> ['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
print(tuple(a))--> ('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
print(set(a))--> {'c', 'o', 'd', 'e', 'g', 'n', 'a', 'n'}

print(dict(a)) #ERROR  we can possible by using fromkeys() method


#Dict method
#FROMKEYS() METHOD
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"pooja")
print(c)

c["d"]="sam"
print(c)'''



#Old user_method

'''while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)

while True:
    a=float(input("a value:"))
    b=int(input("a value:"))
    print(a+b)


while True:
    a=(input("a value:"))
    b=(input("a value:"))
    print(a+b)                


while True:
    a=complex(input("a value:"))
    b=complex(input("a value:"))
    print(a+b)


while True:
    a=bool(input("a value:"))
    b=bool(input("a value:"))
    print(a+b)'''



#BUILT-IN FUNCTIONS
#1.eval()
#2.zip()
#3.enumerate()
#4.ASCII built-in Functions

#eval() built-in function
#By using eval() built-in function we can in single code
#eval() method is to accept Normal Datatypes in single code                 
'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''



#zip()--> we can combine multiple collections into one collection
    
#merging
'''a=[10,20,30,40,50]
names=["teja","dinesh","vamsi","sanklap","surya"]
print(a+names)
       
#zip() method usage

b=zip(a,names)
print(b)

b=list(zip(a,names))
print(b)
      
       
b=list(zip(a,names))
print(b)                 

b=tuple(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''


#enumerate() -->we can give counter to the collection

'''names=["mythri","darshi","sarvani","srivarna","tejaswani"]

#Normal method
for i in range (len(names)):
    print(i,names[i])
#o/p-->
0 mythri
1 darshi
2 sarvani
3 srivarna
4 tejaswani    
    
#By using enumerate()

b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)

{100: 'mythri', 101: 'darshi', 102: 'sarvani', 103: 'srivarna', 104: 'tejaswani'}

b=set(enumerate(names,100))
print(b)

{(103, 'srivarna'), (100, 'mythri'), (101, 'darshi'), (104, 'tejaswani'), (102, 'sarvani')}

b=tuple(enumerate(names,100))
print(b)

((100, 'mythri'), (101, 'darshi'), (102, 'sarvani'), (103, 'srivarna'), (104, 'tejaswani'))

b=list(enumerate(names,100))
print(b)

[(100, 'mythri'), (101, 'darshi'), (102, 'sarvani'), (103, 'srivarna'), (104, 'tejaswani')]'''



#ASCII --> AMERICAN STANDARD CODE INFORMATION INTERCHANGE
#In ASCII we have two types:
#1.chr() --> we can pass only numbers
#2.ord() --> we can pass only alphabets

#chr()
'''print(chr(65))

print(chr(90))

print(chr("a"))

print(chr(91))

#ord()
print(ord("a"))

print(ord("z"))

print(ord(56))'''

#TASK
#print A to Z
#print a to z

'''for i in range(65,91):
    print( chr(i),end=" ")
    
for i in range(97,123):
    print( chr(i),end=" ")
      
a=input("enter the name:")
for i in a:
    print(i,"-",ord(i))'''


#max()--> Highest value
#min()--> lowest value
#sum()--> sum of the value

'''print(max(2,5,8,9,10,20,30))


print(min(2,5,8,9,10,20,30))

    
#print(sum(2,5,8,9,10,20,30))  #TypeError: sum() takes at most 2 arguments (7 given)

a=2,3,4,5,6,7,9
print(sum(a))'''



#TASK
 
#MARKS ANALYSIS REPORT                                                              

#BY USING FUNCTIONS

def get_marks():
    n = int(input("Enter total number of students: "))
    marks = []

    for i in range(n):
        mark = int(input(f"Enter Student {i+1} Marks: "))
        marks.append(mark)



    return marks


def report(marks):
    print("\n----- MARKS REPORT -----")
    print("Total Students :", len(marks))
    print("Highest Marks  :", max(marks))
    print("Lowest Marks   :", min(marks))
    print("Total Marks    :", sum(marks))
    print("Average Marks  :", sum(marks) / len(marks))


marks = get_marks()
report(marks)










'''# Read total number of students
n = int(input("Enter total number of students: "))

# Empty list to store marks
marks = []

# Read marks
for i in range(n):
    mark = int(input(f"Enter Student {i+1} Marks: "))
    marks.append(mark)

# Find report details
total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
total_marks = sum(marks)
average_marks = total_marks / total_students

# Display report
print("\n----- MARKS REPORT -----")
print("Total Students :", total_students)
print("Highest Marks  :", highest_marks)
print("Lowest Marks   :", lowest_marks)
print("Total Marks    :", total_marks)
print("Average Marks  :", average_marks)'''
