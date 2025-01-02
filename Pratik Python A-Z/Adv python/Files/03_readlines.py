f=open("write.txt")

"""
lines=f.readlines()
print(lines , type(lines)) # is is a list type 

"""
# For accessing all the lines one by one 
l1=f.readline()
print(l1)
l2=f.readline()
print(l2)
l3=f.readline()
print(l3)
l4=f.readline()
print(l4)
l5=f.readline()
print(l5) # 5th line is not present is show nothing
# proof
print(l5 =="") #it will show true

#  print it all at onces 
l=f.readline()
while (l !=""):
    print(l)
    l=f.readline()
f.close()