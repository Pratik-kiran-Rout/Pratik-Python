import random
def game(x,y):
    print("you are playing the game ")
    #number = random.randint(1,100)
    maxand = x&y 
    f=open("hiscore.txt")
    score=f.read()#it store in string form in a file 
    if score!="":#it means that empty
        score =int(score)
    else: score=0
    # Now find the highest AND value
    with open("hiscore.txt","w") as i:
        if maxand > score or score==0:
            i.write(str(maxand))
    return maxand

x=int(input("Enter 1st number  "))
y=int(input("Enter 1st number  "))
max = game(x,y)
print(max)

