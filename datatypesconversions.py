Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes conversions
#int()
int(9)
9
int(8.9)
8
int("chaithu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("chaithu")
ValueError: invalid literal for int() with base 10: 'chaithu'
int(6=9j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
>>> flat(3.9)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    flat(3.9)
NameError: name 'flat' is not defined. Did you mean: 'float'?
>>> float(3.9)
3.9
>>> float(7+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(7+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(7+9j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(7+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> flat("python")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    flat("python")
NameError: name 'flat' is not defined. Did you mean: 'float'?
>>> float(True)
1.0
>>> float(False)
0.0
>>> #str()
>>> str(6)
'6'
>>> str(5.6)
'5.6'
>>> str("hi")
'hi'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(7.8)
(7.8+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
complex(5+7j)
(5+7j)
complex(True)
(1+0j)
cpmplex(False)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    cpmplex(False)
NameError: name 'cpmplex' is not defined. Did you mean: 'complex'?
complex(False)
0j
#bool
bool(4)
True
bool(8.9)
True
bool("java")
True
bool(True)
True
bool(False)
False
