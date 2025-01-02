import math
class calculator:
    def __init__(self,num) -> None:
        self.num=num
        self.squareroot=math.sqrt(num)
        self.cube = math.pow(num,3) #or you can use num**3
        self.square = math.pow(num,2)
x=int(input("Enter the number ! :"))
calculate = calculator(x)
print(f"The square is {calculate.square} , the square root is {calculate.squareroot} and the cube is {calculate.cube}")