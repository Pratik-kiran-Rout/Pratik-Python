class complexNum:
   def __init__(self,real,imag) -> None:
      self.real=real
      self.imag=imag
   
   def __add__(num1,num2):
      return complexNum((num1.real + num2.real),(num1.imag + num2.imag))
   
   def __sub__(num1,num2):
      return complexNum((num1.real - num2.real),(num1.imag - num2.imag))
      
   def __str__(self):
      return f"{self.real} + {self.imag}i"
n1=complexNum(2,3)
n2=complexNum(4,5)
print(n1 + n2)
print(n1 - n2)

"""
class complex:
   def __init__(self,real,imag) -> None:
      self.real=real
      self.imag=imag
   
   def __add__(num1,num2):
      return complex((num1.real + num2.real),(num1.imag + num2.imag))
   
   def __sub__(num1,num2):
      return complex((num1.real - num2.real),(num1.imag - num2.imag))
      
   def __str__(self):
      return f"{self.real} + {self.imag}i"
n1=complex(2,3)
n2=complex(4,5)
print(n1 + n2)
print(n1 - n2)

"""