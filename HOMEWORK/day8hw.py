# Base class
class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")

# Trainer class inherits from Employee
class Trainer(Employee):
    def __init__(self, name: str, role: str, specialization: str):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")

# YogaInstructor class inherits from Employee
class YogaInstructor(Employee):
    def __init__(self, name: str, role: str, yoga_style: str):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")

# MultiTrainer inherits from both Trainer and YogaInstructor
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name: str, role: str, specialization: str, yoga_style: str):
        Trainer.__init__(self, name, role, specialization)
        YogaInstructor.__init__(self, name, role, yoga_style)

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")

# Creating objects
employee = Employee("Ravi", "Receptionist")
trainer = Trainer("Anita", "Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Karan", "MultiTrainer", "Cardio", "Vinyasa Yoga")

# Displaying details
print("Employee Details:")
employee.display()

print("\nTrainer Details:")
trainer.display()

print("\nYoga Instructor Details:")
yoga_instructor.display()

print("\nMultiTrainer Details:")
multi_trainer.display()