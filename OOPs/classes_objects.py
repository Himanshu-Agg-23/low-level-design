class Student:
    # class variables (attributes)
    name = ""
    age = 0
    gender = ""

    def __init__(self, name : str="", age: int=0, gender: str="") -> None:
        # __init__ is a special method that is called when an object is created
        # it is the constructor of the class and is used to initialize the attributes of the object
        self.name = name
        self.age = age
        self.gender = gender

    # class method
    def display_info(self) -> None:
        #self is a reference to the current instance of the class
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


s1 = Student("Alice", 20, "Female")
s1.display_info()

s2 = Student("Bob", 22, "Male")
s2.display_info()