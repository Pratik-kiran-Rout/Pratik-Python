class vechile:
   def __init__(self,company,model) -> None:
      self.company=company
      self.model=model
class car(vechile):
   def __init__(self, company, model,doors) -> None:
      super().__init__(company, model)
      self.doors=doors

   def show(self):
      print(f"The car company {self.company} and model {self.model} and number of doors are {self.doors}")

obj=car("Bmw","M8",4)
obj.show()