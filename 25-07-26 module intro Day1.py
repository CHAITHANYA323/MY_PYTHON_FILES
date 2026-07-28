
#BY USING FUNCTION
def greetings(name):
    print("welcome",name)
#BY USING VARAIBLES &PRINT FUNCTION    
a=3
b=8
print("the sum is a+b")

#BY USING USER_INPUT 
a=int(input("a value"))
b=int(input("b value"))
print(a+b)

#BY USING DICT 
details={"idnos":[10,20,30],
         "names":["sampth","vamsi","bhanu"],
         "marks":[60,70,90]}



#DIFFERENCE B/W MODULE & SCRIPT

if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)

def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this  program  is run as module")
dummy()        

o/p-->this program is run as script        
