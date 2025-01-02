class emplyee:
    comapanyName ="Infosys"
    name ="Pratik.K Rout"
    salery = 1500000
    def company (self):
          print(f"The name of the emplyee {self.name} , company is {self.company} and the salery is {self.salery} ")
class coder(emplyee):# now coder is inherite from the emplyee which is a single inheritance 
     language = " Machine learing "
     def langu(self):
          print(f"The language is {self.language}")

obj = coder()
obj.salery
obj.company()
obj.language() # we can acess the each attributes from the inherited class
obj.langu()