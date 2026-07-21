#GENERATORS

#DIFFERENCE B/W LIST COMPREHERSION AND GENEATORS

#a=[expr for var in collection/range]

'''a=[i for i in range(21)]
print(a)
print(type(a))'''

#a=(expr for var in collection/range)
a=(i for i in range(21))
print(a)  #ERROR (<generator object <genexpr> at 0x000001A769A88E10>)
print(*a)
print(type(a))

print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#NOT WORK


#BY USING Yield BUILT-IN FUNCTION
a,b=(int(x) for x in inout("enter the values").split(",")
def check(a,b):
    while a<b:
        yield a
        a=a=a+1
        yield a
print (*check (a,b))

#BY USING Return BUILT-IN FUNCTION
a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check (a,b))


#EXAMPLES FOR Yield  V/S Return

def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    return "vja" "hyd" "vzg"
print(*mygen())

def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))# stop iteration










