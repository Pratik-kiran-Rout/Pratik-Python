""" f=open("file.txt")
print(f.read())
f.close() """

#   same this we can write by using the with statement 
with open("file.txt") as f:
    print(f.read())
#   here we dont need any kind of close 