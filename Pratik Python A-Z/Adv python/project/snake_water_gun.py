"""
Here we take
1 for snake 
-1 for water
0 for gun 

"""
import random
#  let 
computer = random.choice([-1,1,0])
you=input("Enter your choice : s,w,g : ")
dic ={ "s":1 , "w":-1 , "g":0}
choice = dic[you] # you contain 1 , -1 , 0

value ={1:"SNAKE", -1:"WATER" , 0:"GUN"}
# Here two variables are there " choice " and " computer "
print(f" your choice is {value[choice]} and computer choice is {value[computer]} ")

if choice == computer:
    print("Draw !")
else:
    if choice ==1 and computer ==-1: # computer - you = -1-1=-2
        print("you win !")
    elif choice ==0 and computer ==1:# 1
        print(" you win !")
    elif choice ==-1 and computer ==0: #1
        print(" you win !")
    elif choice ==0 and computer ==-1: #-1
        print(" computer win !")
    elif choice ==1 and computer ==0: #-1
        print(" computer win !")
    elif choice ==-1 and computer ==1: #2
        print(" computer win !")
    else :
        print("Enter valid choice")

        #  it also valid not not that much readable 
    

#  you only win when computer - your choice == 1 or -2 
"""
   if(computer - choice)== 1 or (computer - choice)== -2:
      print("YOU WIN !")
   else:
      print("COMPUTER WIN !")

"""