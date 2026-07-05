Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"pooja","year":2020,"month":6}
>>> print(a)
{'name': 'pooja', 'year': 2020, 'month': 6}
>>> type(a)
<class 'dict'>
>>> b={"name","chaithu"}
>>> type(b)
<class 'set'>
>>> c={2027:7}
>>> type(c)
<class 'dict'>
>>> 
>>> #update method
>>> a={"year":2026,"month":"july","date":4}
>>> a.update({"time:7})
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> a.update({"time":7})
...           
>>> a
...           
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7}
>>> a.update({"name":"chaithu"},{city:"vja"})
...           
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.update({"name":"chaithu"},{city:"vja"})
NameError: name 'city' is not defined
>>> a.update({"name":"chaithu",city:"vja"})
...           
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.update({"name":"chaithu",city:"vja"})
NameError: name 'city' is not defined
>>> a.update({"name":"chaithu","city":"vja"})
...           
>>> a
...           
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'chaithu', 'city': 'vja'}
>>> 
>>> #setdefault method
...           
>>> a={"course":"pyhton"}
...           
a.setdefault("duration",4)
          
4
a
          
{'course': 'pyhton', 'duration': 4}

#accessing value method
          
a{"colour":"black","food":"biryani","icecream":"nuts"}
          
SyntaxError: invalid syntax
a={"colour":"black","food":"biryani","icecream":"nuts"}
          
a["colour"]
          
'black'
a["black"]
          
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a["black"]
KeyError: 'black'
a.get("food")
          
'biryani'
a
          
{'colour': 'black', 'food': 'biryani', 'icecream': 'nuts'}
a.get("biryani")
          
a
          
{'colour': 'black', 'food': 'biryani', 'icecream': 'nuts'}

