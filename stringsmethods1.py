Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings methods
#len()
a="python"
len(a)
6
b="python course"
len (b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twonklw little star"
counnt("twinkle")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    counnt("twinkle")
NameError: name 'counnt' is not defined
count("twinkle")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count("twinkle")
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle)
        
SyntaxError: unterminated string literal (detected at line 1)
>>> a.count("twinkle")
...         
1
>>> a.count("t")
...         
5
>>> a.count(" ")
...         
3
>>> b="twinkletwinkle"
...         
>>> b.count("twinkle")
...         
2
>>> b.count("twinkletwinkle")
...         
1
>>> #find a string
...         
>>> a="python"
...         
>>> a[2]
...         
't'
>>> a.find("t")
...         
2
>>> a.find("n")
...         
5
>>> b=("hello")
...         
>>> b="hello"
...         
>>> b.find("l")
...         
2
>>> b[2:4]
...         
'll'
>>> a.find("m")
...         
-1
>>> #escape sequences
...         
>>> #\n->new line
        
#\t->tab space (in btwn 4 to 8 spaces)
        
a="name\nmobileno\tmailid\ncollege\tbranch"
        
print(a)
        
name
mobileno	mailid
college	branch
b="name:chaithu\nmobileno:6456783456\tmailid:chaithu@gmail.com\n collegename:Au\tbranch:cse"
        
print(b)
        
name:chaithu
mobileno:6456783456	mailid:chaithu@gmail.com
 collegename:Au	branch:cse
#replace()
        
b.replace()
        
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b.replace()
TypeError: replace() takes at least 2 positional arguments (0 given)
a="wait until you succeed"
        
a.replace("wait","work")
        
'work until you succeed'
b="i love java"
        
b.replace("java","python")
        
'i love python'
#upper()
        
a="hello"
        
a.upper()
        
'HELLO'
b="HII"
        
b.lower()
        
'hii'
c="python"
        
c.upper("P")
        
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c.upper("P")
TypeError: str.upper() takes no arguments (1 given)
c.upper("p")
        
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
        
'P'
c.capitalize()
        
'Python'
d="python course"
        
d.title()
        
'Python Course'
e="i am in class"
        
e.capitalize()
        
'I am in class'
e.title()
        
'I Am In Class'
a="python"
        
a.isupper()
        
False
a.islower()
        
True
a.isalpha()
        
True
b="python course"
        
b.isalpha()
        
False
c="python coouse()
        
SyntaxError: unterminated string literal (detected at line 1)
c="python course"
        
e=1234
        
e.isdigit()
        
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    e.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="1234"
        
e.isdigit()
        
True
f="pooja"
        
f.isalnum()
        
True
g="1234"
        
f.isalnum()
        
True
h="pooja@123"
        
h.isalnum()
        
False
x="pooja_123"
        
x.isalnum()
        
False
#string with &endswith
        
a="java"
        
a.startswith(j)
        
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.startswith(j)
NameError: name 'j' is not defined
a="java"
        
a.startswith("j")
        
True
a.endswith("h")
        
False
#strip()
        
#lstrip(),rstrip()
        
a="        chaithu         "
        
a.strip()
        
'chaithu'
a.lstrip()
        
'chaithu         '
a.rstrip()
        
'        chaithu'
#split()
        
a="python java c c++"
        
a.split()
        
['python', 'java', 'c', 'c++']

b="i am in class room"
        
b.split()
        
['i', 'am', 'in', 'class', 'room']
#join()
        
b="vja","hyd","vzg"
        
join(b)
        
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    join(b)
NameError: name 'join' is not defined
"".join(b)
        
'vjahydvzg'
" ".join(b)
        
'vja hyd vzg'
"k".join(b)
        
'vjakhydkvzg'
c="python"
        
"k".join(c)
        
'pkyktkhkokn'
