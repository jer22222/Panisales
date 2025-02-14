class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by ${amount}. New salary: ${self.salary}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

employee = Employee("ALjon", "Software Developer", 10000)

employee.give_raise(10000)
print()
employee.display_employee()
