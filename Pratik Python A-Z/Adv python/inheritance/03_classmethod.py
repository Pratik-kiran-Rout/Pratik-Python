# class calculator :
#    a=10
#    def show(self):
#       print(f"The number in the class attributes is {self.a} ")
# obj=calculator()
# obj.a=50
# obj.show() #it will show the obj attributes 
      
class calculator :
   a=10
   @classmethod
   def show(self):
      print(f"The number in the class attributes is {self.a} ")
obj=calculator()
obj.a=50
obj.show() # 10
#it will show the class attributes because the show is declared as @classmethod