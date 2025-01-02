#  for appending the string at the end of the file
""" 
here we use "a" in the open in the sec parameter 

"""
st="Hello , knock knock !"
f=open("write.txt","a") # here "a" use for append operation 
f.write(st)  #it will add to that file 
f.close()
