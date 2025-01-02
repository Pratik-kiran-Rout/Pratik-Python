class emplyee:
    name = "rohan"
    salery = 1300000
    language = "python"

    def __init__(self,name,salery,language) -> None:
        print("Here is the information regarding the emplyee")
        self.name=name 
        self.saley = salery
        self.language = language

    @staticmethod
    def greet():
        print("HELLO GOOD MORING SIR !AND HAVE A NICE DAY:)")

class emplyee_1:
    name = "rohan"
    salery = 1300000
    language = "python"

    def __init__(self,name,salery) -> None:
        #print("Here is the information regarding the emplyee")
        self.name=name 
        self.saley = salery
        #self.language = language


    @staticmethod
    def greet():
        print("HELLO GOOD MORING SIR !AND HAVE A NICE DAY:)")


pratik=emplyee("pratik",1500000,"machine learning") 
rohan =emplyee_1("rohan",1200000) #b/c here we dont pass any kind of language

#at the time of object creation the _ init _ funtion is automatically CALLED
pratik.greet()
#if there we dont pass any langauge then it display the class attributes
print(f"The name {pratik.name} , salery is {pratik.salery} and the language is {pratik.language}")

rohan.greet()
print(f"The name {rohan.name} , salery is {rohan.salery} and the language is {rohan.language}")
#it defaultly show the python language
    