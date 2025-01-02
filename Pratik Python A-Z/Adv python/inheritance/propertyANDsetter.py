class employee:
    a = 10  # Class attribute (shared by all instances)

    @classmethod
    def show(self):
        print(f"The value is {self.a}")  # Prints the class attribute 'a'

    @property # it is a getter 
    def name(self):  # Property (getter) method
        return f"{self.lname} {self.fname}"  # Returns the full name as "last name first name"
    
    @name.setter  # it also use for the encapsulation 
    def name(self, Name):  # Setter method for the 'name' property
        self.fname = Name.split()[0]  # Splits the full name and assigns the first part to 'fname'
        self.lname = Name.split()[1]  # Assigns the second part to 'lname'

# Create an instance of the class
obj = employee()

# Change instance attribute 'a'
obj.a = 50  # This changes the 'a' for this instance, but does not change the class-level 'a'

# Set the full name using the setter
obj.name = "pratik kiran"  # Invokes the setter to split the name

# Print the full name using the getter
print(f"The name is {obj.name}")  # Invokes the getter to return the name

"""class empolyee:
   a=10
   @classmethod
   def show(self):
      print(f"The value is {self.a}") # it will show the class attributes

   @property #also know as getter 
   def name(self): #called 2nd  8 --> 18
      return f"{self.lname} {self.fname}"
   @name.setter
   def name (self,Name): # 1st called 11 --> 8
      self.fname = Name.split()[0]
      self.lname = Name.split()[1]
   
obj = empolyee()
obj.a=50 # it dont show because of the class method 
obj.name = "pratik kiran" # 17 --> 11
print(f"The name is {obj.name} ") """
