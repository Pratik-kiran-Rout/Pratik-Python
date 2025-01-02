class emplyee:
    salery = 1200000
    language = " python "

    def info(self):
        print(f"The salery is {self.salery} and the language is {self.language}")
    
    # so we decladed this gree as static method 
    @staticmethod #syntex for static method 
    def greet():# here we dont need any kind of parametrer to pass so we
        print("Good moring pratik :)")

pratik=emplyee()
pratik.language = " java script" #now it display object attributes " java script"
pratik.info()
pratik.greet()