class programmer():
    def __init__(self,name,salery,language) -> None:
        self.name=name
        self.salery=salery
        self.language =language
    
emp1=programmer("pratik","1500000","machine learning")
print(f"EMPLYEE NAME IS {emp1.name} salery is {emp1.salery} and the lamguage is {emp1.language}")
emp2 =programmer("rohan",1200000,"python")
print(f"EMPLYEE NAME IS {emp2.name} salery is {emp2.salery} and the lamguage is {emp2.language}")