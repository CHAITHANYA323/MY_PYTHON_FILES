Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[0]
'v'
a[5]
'a'
a[1]
'i'
 a[0]+a{1]+a[2]+a[3]+a[4]+a[5]
 
SyntaxError: unexpected indent
a[0]+a{1]+a[2]+a[3]+a[4]+a[5]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
 a[8]+a{9]+a[10]+a[11]+a[12]
 
SyntaxError: unexpected indent
a[8]+a{9]+a[10]+a[11]+a[12]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a="simple is better than complex"
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[o]+a[1]+a[2]+a[3]+a[4]+a[5]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[o]+a[1]+a[2]+a[3]+a[4]+a[5]
NameError: name 'o' is not defined
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[22]+a[23]+a[24]+a[25]+a[26]
'compl'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
a="codegnan it solutions"
a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
' solution'
a[9]+a[10]
'it'
a[0]+a{1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]
'codegnan'
 #negative indexing
a="i am learning python'
SyntaxError: unterminated string literal (detected at line 1)
a="i am learning python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]+a[-9]+a[-8]
'learning'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
a[-19]+a[-16]+a[-7]
'   '
a="python fullstack"
a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'stack'
a[-9]+a[-8]+a[-7]+a[-6]
'full'
a[16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a[16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
IndexError: string index out of range
a[-16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'python'

#slicing concept
a=""codegnan"
SyntaxError: unterminated string literal (detected at line 1)
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4;]
SyntaxError: invalid syntax
a[4:]
'gnan'
a="time is veru precious"
a[8;12]
SyntaxError: invalid syntax
a[8:12]
'veru'
a[0:4]
'time'
a[13:21]
'precious'
a="work until you succeed"
a[15:21]
'succee'
a[15:22]
'succeed'
a[5:10]
'until'
a[11:14]
'you'
a[0:4]
'work'
#negative slicing
a="vizaf is city of destiny"
a="vizag is city of destiny"
a[15:-11]
''
a[-15:-11]
'city'
a[-7:-1]
'destin'
a[-7:]
'destiny'
a[-24:-19]
'vizag'
b="hi hello how are you"
>>> a[-17:-12]
's cit'
>>> b[-17:-12]
'hello'
>>> b[-11:-8]
'how'
>>> b[-7:-4]
'are'
>>> KeyboardInterrupt
>>> b[-3:]
'you'
>>> KeyboardInterrupt
>>> b[-20:-18]
'hi'
>>> 
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a=[::2]
SyntaxError: invalid syntax
>>> a[::2]
'dt cec'
>>>  a="machine learning"
...  
SyntaxError: unexpected indent
>>> a="machine learning"
>>> a[1:5]
'achi'
>>> a[::5]
'mnag'
>>> a[::7]
'm n'
>>> a="cloud computing"
>>> a[1:9:2]
'lu o'
>>> a[2:13:3]
'o mt'
>>> a[6:14:4]
'cu'
>>> a[5:12:2]
' opt'
>>> a[3:9:5]
'um'
