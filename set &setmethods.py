Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={3,6.7,"python",8+9j,True,Flase}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a={3,6.7,"python",8+9j,True,Flase}
NameError: name 'Flase' is not defined. Did you mean: 'False'?
print(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
a={3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 3, (8+9j), 'python', 6.7}
type(a)
<class 'set'>
b={6,9,3,5,10,9,20,5)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
b={6,9,3,5,10,9,20,5}
print(b)
{3, 20, 5, 6, 9, 10}

#subset method
a={2,3,45,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False

#superset method

#union method
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection method
a={3,4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}

#difference
a={10,11,12,1,3,14,15,16}
b={6,7,8,12,1,3,14,15,16,17}
a.difference(b)
{10, 11}
b.difference(a)
{8, 17, 6, 7}

#symmetric difference
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}

#update
a={1,2,3,4,5}
b={4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection_update
a={1,3,5,6,7,8,10}
b={2,4,56,7,10,11,12}
a
{1, 3, 5, 6, 7, 8, 10}
a.intersection_update(b)
a
{10, 7}
a
{10, 7}
b.intersection_update(a)
b
{10, 7}
b
{10, 7}

#difference_update
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.diiference_update(b)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.diiference_update(b)
AttributeError: 'set' object has no attribute 'diiference_update'. Did you mean: 'difference_update'?
a.difference_update(b)
a
{2, 3, 4}
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9, 10}
b
{1, 5, 6, 7, 8, 9, 10}

#symmetric_difference_update
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference(b)
{2, 3, 4, 10, 11}
a
{2, 3, 4, 5, 6, 7, 8, 9}
b.symmetric_difference_update(a)
b
{2, 3, 4, 10, 11}
b
{2, 3, 4, 10, 11}

#add method
a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}

#copy method
a={3,4,5,6,7,8}
a.copy()
{3, 4, 5, 6, 7, 8}
b=a.copy()
b
{3, 4, 5, 6, 7, 8}

#clear method
a={3,4,5,6,7,8}
a.clear()
a
set()
c=set()
c.add(30)
c
{30}

#pop method
a={5,6,7,8,9}
a.pop()
5
a.pop(7)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
a.remove(7)
>>> a
{6, 8, 9}
>>> 
>>> #discard and remove same
>>> a{2,3,4,5,6}
SyntaxError: invalid syntax
>>> a={2,3,4,5,6,}
>>> a.discard(4)
>>> a
{2, 3, 5, 6}
>>> 
>>> #isdisjoint method
>>> a={2,3,4,5,6,}
>>> b={4,5,6,7,}
>>> c={8,9,10,11,12}
>>> b.isdisjoint(a)
False
>>> b.isdisjoint(c)
True
>>> 
>>> #length method
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> 
>>> #count method
>>> a={4,5,6,7,8}
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #index method
>>> a={4,5,6,7,8}
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> 
>>> #Task
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[8]+a[6]+a[5]+a[7]+a[9]+a[0]+a[4]+a[2]+a[3]+a[1]
45
