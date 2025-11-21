# Base class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Employee class inherits from Person
class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# PartTime class inherits from Person
class PartTime(Person):
    def __init__(self, name: str, age: int, working_hours: float):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")

# Consultant class inherits from both Employee and PartTime
class Consultant(Employee, PartTime):
    def __init__(self, name: str, age: int, employee_id: str, working_hours: float, project_name: str):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, Project Name: {self.project_name}")

# Creating objects
person = Person("Alice", 30)
employee = Employee("Bob", 35, "E123")
part_time = PartTime("Charlie", 28, 20.5)
consultant = Consultant("Diana", 40, "C456", 15.0, "AI Development")

# Displaying details
print("Person Details:")
person.show_details()

print("\nEmployee Details:")
employee.show_details()

print("\nPart-Time Worker Details:")
part_time.show_details()

print("\nConsultant Details:")
consultant.show_details()