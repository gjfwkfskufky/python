class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(
            f"Name: {self.name}, Role: {self.role}, "
            f"Specialization: {self.specialization}, "
            f"Yoga Style: {self.yoga_style}"
        )


e = Employee("Alex", "Staff")
t = Trainer("Brian", "Trainer", "Strength Training")
y = YogaInstructor("Clara", "Yoga Instructor", "Hatha Yoga")
m = MultiTrainer("Diana", "Multi Trainer", "Cardio", "Vinyasa")

e.display()
t.display()
y.display()
m.display()
