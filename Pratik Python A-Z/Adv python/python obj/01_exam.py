class Emplyee:
    language = "Python"  #object attributes
    salery = 1500000

# object creation 
pratik = Emplyee()

# by using the object we can add any new variable 
pratik.name="pratik kiran rout " #object/instance attributes
print(pratik.name,pratik.salery , pratik.language)

rohon= Emplyee()
rohon.name ="Rohan patra "
# also we can display it
print(rohon.name ,rohon.language,rohon.salery)

"""
 here "name" is a object / instance  Attribute and "salery" and " language " is 
 a class attributes because it directly belongs to the class 
"""