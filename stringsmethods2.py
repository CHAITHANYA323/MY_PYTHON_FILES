Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#contentation
a-"code"
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a-"code"
NameError: name 'a' is not defined
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+" "+b)
python course
fname="chaithu"
lname="k"
print(fname+lname)
chaithuk
print(fname+" "+lname)
chaithu k
print(fname.title()+" "+lname.title())
Chaithu K
print(fname+" "+lname).title()
chaithu k
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Chaithu K

#formstting
#formatting
a=2
b=4
print(a+b)
6
print("the sum is ",a+b)
the sum is  6
city="vja"
print("the city is",city)
the city is vja

#format method()
a="motu"
b"pathlu"
b'pathlu'
b="pathlu"
print("hello {}{}.format(a,b))
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello {}{}".format(a,b))
      
hello motupathlu
print("hello {}{}".format(a,b))
      
hello motupathlu
print("hello {} {}".format(a,b))
      
hello motu pathlu

print("hello {} hii {}".format(a,b))
      
hello motu hii pathlu

#fstring()
      
a="sita"
      
b="ram"
...       
>>> print(f"hello {a}{b}")
...       
hello sitaram
>>> print(f"hello {a} {b}")
...       
hello sita ram
>>> print(f"hello {a}  hii {b}")
...       
hello sita  hii ram
>>> 
>>> #task multiplication program
...       
>>> a=5
...       
>>> b=8
...       
>>> print("multiplication is",a*b)
...       
multiplication is 40
>>> KeyboardInterrupt
>>> print("multiplication {}{}".format(a,b))
...       
multiplication 58
>>> print(f"muliplication is {a} {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> rint(f"muliplication is {a} {b}")
...       
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    rint(f"muliplication is {a} {b}")
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> print(f"muliplication is {a} {b}")
...       
muliplication is 5 8
>>> print(f"muliplication is {a}{b}")
...       
muliplication is 58
>>> a=5
...       
>>> b=9
...       
>>> print(a*b)
...       
45
>>> c=a*b
      
print("the product is {}".format(c))
      
the product is 45
print(f"the is product is {}")
      
SyntaxError: f-string: valid expression required before '}'
print(f"the is product is {c}")
      
the is product is 45
print("the product is {}",format(a*b))
      
the product is {} 45
print("the product is {a*b}")
      
the product is {a*b}
print(f"the product is {a*b}")
      
the product is 45
