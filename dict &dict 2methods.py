Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,7,3,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
>>> #keys,values,items methods
>>> 
>>> a={"month":7,"day":"sat","time":7}
>>> a.keys()
dict_keys(['month', 'day', 'time'])
>>> dict_keys([month":7,"day":"sat","time":7])
...            
SyntaxError: unterminated string literal (detected at line 1)
>>> a.values()
...            
dict_values([7, 'sat', 7])
>>> a.items()
...            
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])
>>> 
>>> #pop method
...            
>>> a={"city":"vij","country":"india","state":"ap"}
...            
>>> a.pop()
...            
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
           
'vij'
a.popitem()
           
('state', 'ap')

a
           
{'country': 'india'}

a={"name":"chaithu","mail":"chaithu@gmail.com"}
           
len(a)
           
2
a.copy()
           
{'name': 'chaithu', 'mail': 'chaithu@gmail.com'}
a
           
{'name': 'chaithu', 'mail': 'chaithu@gmail.com'}
b=a.copy()
           
b
           
{'name': 'chaithu', 'mail': 'chaithu@gmail.com'}
a.clear()
           
a
           
{}

a={"name":"chaithu","year":2020,"name":"chaithu"}
           
print(a)
           
{'name': 'chaithu', 'year': 2020}
a={"name":"chaithu","year":2020,"name":"raju"}
           
print(a)
           
{'name': 'raju', 'year': 2020}
a={"name1":"chaithu","year":2020,"name2":"raju"}
           
print(a)
           
{'name1': 'chaithu', 'year': 2020, 'name2': 'raju'}

   
a={"idnos":[10,20,20],"names":["sweety","cuty","hearty"],"marks":[60,70,80]}
           
print(a)
           
{'idnos': [10, 20, 20], 'names': ['sweety', 'cuty', 'hearty'], 'marks': [60, 70, 80]}
a.keys()
           
dict_keys(['idnos', 'names', 'marks'])
a.values()
           
dict_values([[10, 20, 20], ['sweety', 'cuty', 'hearty'], [60, 70, 80]])
a.items()
           
dict_items([('idnos', [10, 20, 20]), ('names', ['sweety', 'cuty', 'hearty']), ('marks', [60, 70, 80])])

a{"year":2026,"month":7}
           
SyntaxError: invalid syntax
a.count("year")
           
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
a.index("month")
           
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
