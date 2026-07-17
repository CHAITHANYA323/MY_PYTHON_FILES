#VARIABLE LENGTH ARGUMENTS

#DATA TYPES USE CHESAM
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={7,8,9,10,11}
check(*c)
d={"year:2026,"month":7}
check(*d)'''

#BY USING CONDITIONS & LOOPS

'''def check(*a):
    d=1  #Creating a Variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,5,4.2,2.5,"chaithu")''' #ONLY EE LINE OKATE ERROR VASTUNDHI


#TASK
'''def check(*a):
    d=1  #Creating a Variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,4.3)
check1(2,3,4,5,4.2,2.5,"chaithu",5+9j,True,False)'''


#KWARGS (OR) KEYWORD ARGUMENTS

'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names"=[harsha","tej","sai"],"marks":{60,70,80},"status":["p","a","p"]}
details(**d)


def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)    #By using for loop ila Rayachu
    for i in a.keys(): #By Using Dict method
        print(i)    
    for i in a:
        print(a[i])  #By using for loop ila Rayachu
    for i in a.values(): #By Using Dict method
        print(i)
    for i in a:
        print(i,a[i])  #By using for loop ila Rayachu
    for i in a.items(): #By Using Dict method
        print(i)
       
details()
d={"names"=[harsha","tej","sai"],"marks":{60,70,80},"status":["p","a","p"]}
details(**d)

#single star and double star in single code usage
#SINGLE  STAR(*) --> TUPLE
#DOUBLE STAR(**) --> DICT
            
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is ",i)
        print("value id ",j)
final()
data=(2,3,4,5,2.3,4.3)
final(*data)
d={"names"=[harsha","tej","sai"],"marks":{60,70,80},"status":["p","a","p"]}
final(**d)
final(*data,**d)'''



#TASK
#Railway Ticket Application

'''TICKET_PRICE = 1000
def calculate_ticket(gender, age):
    if gender == "male":
        if age > 60:
            discount = 30
        else:
            discount = 0

    elif gender == "female":
        if age > 60:
            discount = 50
        else:
            discount = 30

    else:
        print("Invalid Gender")
        return

    final_amount = TICKET_PRICE - (TICKET_PRICE * discount / 100)

    print("\n----- Railway Ticket -----")
    print("Ticket Price :", TICKET_PRICE)
    print("Gender       :", gender)
    print("Age          :", age)
    print("Discount     :", str(discount) + "%")
    print("Amount to Pay:", final_amount)


def main():
    gender = input("Enter Gender (male/female): ").lower()
    age = int(input("Enter Age: "))

    calculate_ticket(gender, age)


main() '''    

           
    

            

            
    



       
   
