# with open("longfile.txt","r") as i:
#     content=i.read()
# if "CSS" in content:
#     print("Found or present !")
# else:print("Not found !")

with open("longfile.txt","r") as i:
    lines =i.readlines()
    lineno =1
for line in lines:
    if "CSS" in line:
           print("Found or present !")
           break
    lineno+=1
else:print("Not found !")
print(f"Found at {lineno}")