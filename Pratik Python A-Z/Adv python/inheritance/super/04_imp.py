class sum:
   def __init__(self,num) -> None:
      self.num=num
      
class multi(sum):
   def __init__( number, num) -> None:
      super().__init__(num)
      number.num=num

   def __mul__(x,y):
      return x.num * y.num
   def __add__(x,y):
      return x.num + y.num

num1=multi(4)
num2=multi(5)
print(num1*num2)

print(num1+num2)