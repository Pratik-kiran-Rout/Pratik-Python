a="String"
a='String'
a='''String'''
## All these three are valid for string
               
               #positive slicing

name="pratik"
stname=name[0:3]
for_only_p=stname[0]
print(stname) # st from 0 to till the end but 3( excluding 3)
print(for_only_p) #v it only print p

       # Negative slicing

name="pratik"
print(name[-4:-1]) # same as print(name[2:5])
print(name[2:5]) #output is same 

print(name[:5]) #same
print(name[0:5])

print(name[0:]) # 0 --> length(6)
print(name[0:len(name)])
print(len(name))

# skip value

a="0123456789"
print(a[1:7:3]) # o/p : "14"

alpha="abcdefghijklmnopqrstuvwxyz"
print(alpha[1:9:4]) 




