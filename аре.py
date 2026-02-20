class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_inf(self):
        print(f"Name: {self.__name}")


class Employer(Human):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def go_to_work(self):
        print(f"{self.name} goes to work")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value


class Student(Human):
    def __init__(self, name, scholarship):
        super().__init__(name)
        self.scholarship = scholarship

    def go_to_lecture(self):
        print(f"{self.name} goes to lecture")

    @property
    def scholarship(self):
        return self.__scholarship

    @scholarship.setter
    def scholarship(self, value):
        if value < 0:
            raise ValueError("Scholarship cannot be negative")
        self.__scholarship = value


class WorkingStudent(Employer, Student):
    def __init__(self, name, salary, scholarship):
        Employer.__init__(self, name, salary)
        Student.__init__(self, name, scholarship)

    def all_activities(self):
        print(f"{self.name} goes to lecture and work")

    def total_income(self):
        return self.salary + self.scholarship


# Демонстрация работы
bob = Employer("Bob", 2500)
bob.go_to_work()
bob.display_inf()
print(f"Salary: {bob.salary}")          # 2500

john = Student("John", 1000)
john.go_to_lecture()
john.display_inf()
print(f"Scholarship: {john.scholarship}")  # 1000

oswald = WorkingStudent("Oswald", 3500, 500)
oswald.all_activities()