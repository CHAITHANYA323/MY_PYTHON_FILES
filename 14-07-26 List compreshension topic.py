#list compreshension
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]

#print(a.upper())

'''b=str(a)
print(b.upper())


for i in a:
    print(i.upper(),end=" ")


b=[]
for i in a:
    b.append(i.upper())
print(b)


#list compreshension syntax

a=[expr for var in collection/range]
a=[i.upper() for i in a]
print(a)'''


#Task-1
'''input=> a=["vja","hyd","vzg"]
output=> ["Vja","Hyd","Vzg"]

    
a=["vja","hyd","vzg"]
a=[i.title() for i in a]
print(a)



#Task-2
a=[1,2,3,4,5,6,7,12,13]
#[1,4,9,25,36,64,144,169]

#method-1
b=[1,2,3,4,5,6,7,12,13]
b=[i**2 for i in b]
print(b)


#method-2
b=[1,2,3,4,5,6,7,12,13]
b=[i*i for i in b]
print(b)

#method-3
b=[1,2,3,4,5,6,7,12,13]
b=[pow(i,2) for i in b]
print(b)


#if-usage in list comprehension

#Task-3

range(16) to print even numbers

c=[i for i in range(16) if i%2==0]
print(a)


range(16) to print odd numbers

a[ i for i in range(16) if i%2!==0]
print(a)


#Task-4

#To print 1 to 20 by using list compreshension
d=[ i for i range(31)]
print(d]


#Task-5

fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]


fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
b=[ i for i in fruits if "a" in i]
print(b)


fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
b=[ i for i in fruits if "a"  not in i]
print(b)


#no-elif usage in list comprehension

#Task-6
#if-else usage in list compreshension

range(21)->even numbers ->squares
range(21)->odd numbers ->multiply 5

a=[i**2 if i%2==0 else i*5 for i range(21)]
print(a)


#Task-7

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]

#method
c=[a[i]+b[i] for i in range(5)]
print(a)

c=[a[i]+b[i] for i in range len(a))]
print(a)'''


#mini project based on completed Topics

#Project Name: ATM Application

account_balance = 100000
card = "c"
password = 1234

insert_card = input("Insert the card: ")

if insert_card == card:
    print("Welcome Pooja")

    enter_password = int(input("Enter the Password: "))

    if enter_password == password:

        print("\nChoose an Option")
        print("1. Balance Enquiry")
        print("2. Withdraw")
        print("3. Exit")

        option = int(input("Enter your option: "))

        if option == 1:
            print("Your Account Balance is:", account_balance)

        elif option == 2:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= account_balance:
                account_balance = account_balance - amount
                print("Please collect your cash.")
                print("Remaining Balance is:", account_balance)
            else:
                print("Insufficient Balance")

        elif option == 3:
            print("Thank You! Visit Again.")

        else:
            print("Invalid Option")

    else:
        print("Incorrect Password")

else:
    print("Invalid Card")




