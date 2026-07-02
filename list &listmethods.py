Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,5.6,"python",9+3j,True,False]
print(a)
[3, 5.6, 'python', (9+3j), True, False]
type(a)
<class 'list'>

#methods in list()
#append()
a{"python","java","c"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a["python","java","c"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a["python","java","c"]
TypeError: list indices must be integers or slices, not tuple
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]

#aextend()
a=["java","html","css"]
a.extend(["js","bs"])
a
['java', 'html', 'css', 'js', 'bs']

#insert()
b=["apple","banana","grapes"]
b.insert(1."mango")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b.insert(1,"mango")
b
['apple', 'mango', 'banana', 'grapes']

#sort()
a=["kiwi","mango","apple","dragon","berry"]
a.sort()
a
['apple', 'berry', 'dragon', 'kiwi', 'mango']
b=[9,6,20,59,72]
b.sort()
b
[6, 9, 20, 59, 72]

#reverse()

a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[3,5,6,7,10]
b
[3, 5, 6, 7, 10]
b=[15,18,16,12,8,5,1]
b
[15, 18, 16, 12, 8, 5, 1]
b.reverse()
b
[1, 5, 8, 12, 16, 18, 15]

#pop()
a={'black","white","red","blue","pink"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["black","white","red","blue","pink"]
   
a
   
['black', 'white', 'red', 'blue', 'pink']
a.pop()
   
'pink'
a
   
['black', 'white', 'red', 'blue']
pop(2)
   
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    pop(2)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
a.pop(2)
   
'red'
a
   
['black', 'white', 'blue']

#remove()
   
a.remove("white")
   
a
   
['black', 'blue']
a=[3,4,5,6,7,8,9]
   
a.pop()
   
9
a.pop(4)
   
7
>>> a
...    
[3, 4, 5, 6, 8]
>>> 
>>> #copy()
...    
>>> a=["pooja","priya","sweety","cuty"]
...    
>>> a.copy()
...    
['pooja', 'priya', 'sweety', 'cuty']
>>> b=a.copy()
...    
>>> b
...    
['pooja', 'priya', 'sweety', 'cuty']
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> b.append()
...    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> b.append("hii")
...    
>>> b
...    
['hii']
>>> b.extend("hello","hii")
...    
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b.extend("hello","hii")
TypeError: list.extend() takes exactly one argument (2 given)
>>> b.extend(["hello","hii"])
...    
>>> b
...    
['hii', 'hello', 'hii']
