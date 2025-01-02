#it contain both the multiple and multilevel inheritance 
class emplyee:
      def __init__(self) -> None:
            print("Constructor of the emplyee !")

class coder(emplyee):# now coder is inherite from the emplyee which is a single inheritance 
      def __init__(self) -> None:
            super().__init__() # it show the methods of the emplyee
            print("Constructor of the coder !")
          
class programmer(): #it inherite both the emplyee and coder 
     
      def __init__(self) -> None:
            print("Constructor of the programmer !")

obj1=emplyee()
obj2 =coder() #it show both the methods of the diffrent class 
obj3 =programmer()