class Sum:
   def __init__(self,n) -> None:
      self.n=n

   def __add__ (num1,num2):
      return num1.n + num2.n

n = Sum(1)
m = Sum(12)
print(n+m)