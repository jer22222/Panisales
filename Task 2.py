class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Aldwin", 20, "Information Technology")
student2 = Student("Hance", 29, "Computer Engineer")
student3 = Student("Rommel", 30, "Information Systems")

student1.introduce()
print()
student2.introduce()
print()  
student3.introduce()
print()

