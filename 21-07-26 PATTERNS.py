
#RIGHT ANGLE PATTERN
n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#REVERSE RIGHT ANGLE PATTERN
row = int(input("Enter the number of rows:"))

for i in range(row, 0,-1):
    for j in range(i):
        print("*", end="")
    print()


# SOLID SQUARE PATTERN
'''
N rows(outer loop), N cols(inner loop)

row col 1 2 3 4 5
    1   * * * * *
    2   * * * * *
    3   * * * * * 
    4   * * * * *
    5   * * * * *
'''

N = int(input('N= '))

for row_num in range(1, N+1):
    for col_num in range(1,N+1):
        print("*",end=" ")
    # new row, new line
    print()

#PYRAMID PATTERN
a=int(input("enter the rows"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("* "*i)    
