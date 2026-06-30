Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=2
b=2
print(a+b)
4
print(a-b)
0
print(a*b)
4
print(a//b)
1
print(a/b)
1.0
print(a**b)
4
print(a%b)
0
#assignment

a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
b+a
8
b+=a
b
8
b-=2
b
6
b*=3
b
18
b//=2
b
9
b/=2
b**=3
b
91.125
b%=2
b
1.125
#assigment updated a
a=3
b=5

print(a+=b)
SyntaxError: invalid syntax
a+b)
SyntaxError: unmatched ')'
(a+b)
8
a+=b)
SyntaxError: unmatched ')'
(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=3
a
5
a*=3
a
15
b//=2
b
2
a
15
a//=2
a
7
a/=2
a
3.5
a**=3
a
42.875
a%=2
a
0.875
#comparision
a=4
b=8
a<b
True
a>b
False
b.a
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b.a
AttributeError: 'int' object has no attribute 'a'
b>a
True
b<a
False
a!=b
True
a==b
False
a=8
b=8
a==b
True
a<=b
True
a>=b
True
b>=a
True
#logical
a=5
b=7
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or a<=b
True
a>=b or a,=b
SyntaxError: cannot assign to expression
a>=b or a<=b
True
a!=b or a==b
True
#identify
a=4
type(a) is int
True
type is not init
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    type is not init
NameError: name 'init' is not defined. Did you mean: 'int'?
type(a) is not int
False
a=5.6
type(a) is float
True
type(a) is not float
False
a="chaithu"
type(a) is str
True
type (a) is not str
False
a=4+3j
type(a) is complex
True
type(a) is not complex
False
a="chaithu"
type(a) is bool
False
type (a) is not bool
True
#membership
a=3,4,5,6,7,8,9,10
3 in a
True
23 in a
False
23 not in a
True
3 not in a
False
#bitwise
a=2
b=8
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(8)
'0b1000'
bin(5)
'0b101'
bin(7)
'0b111'
#or
a=2
b=3
a|b
3
a=4
b=6

a|b
6
bin(6)
'0b110'
bin(4)
'0b100'
#not
a=2
-(a+1)
-3
>>> ~a
-3
>>> a=5
>>> ~a
-6
>>> a=9
>>> ~a
-10
>>> b=-11
>>> ~b
10
>>> c=-15
>>> ~c
14
>>> #xor
>>> a=6
>>> b=9
>>> a^b
15
>>> a=5
>>> b=7
>>> a^b
2
>>> left shift
SyntaxError: invalid syntax
>>> #left shift
>>> a=3
>>> a<<2
12
>>> bin(3)
'0b11'
>>> a=5
>>> a<<3
40
>>> #right shift
>>> a=3
>>> a>>2
0
>>> a=4
>>> a>>2
1
>>> bin(4)
'0b100'
>>> a=9
>>> a>>3
1
