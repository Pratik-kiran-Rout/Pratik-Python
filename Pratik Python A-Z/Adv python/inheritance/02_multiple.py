#it contain both the multiple and multilevel inheritance 
class emplyee:
    comapanyName ="Infosys"
    name ="Pratik.K Rout"
    salery = 1500000
    def company (self): #
          print(f"The name of the emplyee {self.name} , company is {self.comapanyName} and the salery is {self.salery} ")

class coder(emplyee):# now coder is inherite from the emplyee which is a single inheritance 
     language = " Machine learing "
     def langu(self): #
          print(f"The language is {self.language}")
          
class programmer(emplyee,coder): #it inherite both the emplyee and coder 
     def addressdetails(self): #
          print(f"The address of the programmer is {self.address}")
     
obj = programmer()
obj.company() 
obj.langu()
obj.address="balasore"
obj.addressdetails() 