#FILE HANDLING

#WRITE() MODE
'''a=open("chaithu.txt","w")
a.write("codeganan it solutions")
a.close()

a=open("chaithu.txt","w")
a.write("python")
a.close()'''

#APPEND() MODE
'''a=open("chaithu.txt","a")
a.write("python")
a.close()'''


#BY USING_RUN TIME INPUT
#Method-1

'''a=open("chaithu.txt","w")
a.write(input("data"))
a.close()'''

#Method-2
'''a=open("chaithu.txt","w")
b=input("data")
a.write(b)
a.close()'''


#READ() MODE
'''a=open("chaithu.txt")
print(a.read())#-->it will display entire content
#print(a.readline())#--> it will display first line
#print(a.readlines())#-->it will display with \n
#print(read(20))'''


#WRITELINES()
'''names=["sai","raju","srinu","tej","hari"]
a=open("python.txt","w")
a.writelines(names)
a.close()'''

'''names=["sai","raju","srinu","tej","hari"]
a=open("python.txt","w")
a.writelines("\n".join(names))
a.close()'''


'''a=open("C:\\Users\\Lap12NOC\\Desktop\\pythonfiles\\conditions.py")
print(a.read())'''

a=open("09-07-26 conditions (nested-if) day2")
print(a.read())




