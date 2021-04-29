class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first.lower()}.{self.last.lower()}@company.com"
        Employee.num_of_employees += 1

    def get_full_name(self):
        return f"{self.first.capitalize()} {self.last.capitalize()}"

    def apply_raise(self):
        return int(self.pay * Employee.raise_amount)

    @classmethod  # Class methods - cls instead of self
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod  # New Constructor  # Class methods
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # creating a new Employee, we could use Employee(....) instead of cls(....)

    @staticmethod  # Static method - no `self` and no `cls`
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # 5 --> Saturday, 6 --> Sunday
            return False
        return True

    # The method below is mostly for developers usage
    def __repr__(self):  # Can be used to appear instead of object location while printing the object
        return f"Employee '{self.first}', '{self.last}, '{self.last}'"

    # The method below is mostly for users usage
    def __str__(self):  # Can be used to appear instead of object location while printing the object
        return f"{self.get_full_name()} - {self.email}"

    def __add__(self, other):  # Usage -> print(emp1 + emp2)
        return self.pay + other.pay

    def __len__(self):  # can be used for the method __len__
        return len(self.get_full_name())


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Employee.__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_emp(self):
        for employee in self.employees:
            print('---> ' + employee.get_full_name())


dev1 = Developer('Adnan', 'Fahad', 100000, 'Python')
dev2 = Developer('Samir', 'Safi', 40000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 900000, [dev1])
print(mgr_1.email)
mgr_1.add_emp(dev2)  # adding more employees
mgr_1.print_emp()
print('---------------------')
mgr_1.remove_emp(dev1)  # removing employees
mgr_1.print_emp()


# print(dev1.email)
# print(dev1.prog_lang)

print()
print('Notes: ')
print(isinstance(mgr_1, Manager))  # True
print(isinstance(mgr_1, Developer))  # False
print(issubclass(Manager, Manager))  # True
print(issubclass(Developer, Manager))  # False
print(issubclass(Manager, Employee))  # True


emp1 = Employee('Adnan', 'Fahad', 5000)
emp2 = Employee('Salim', 'Fahad', 3000)
# print(emp1.__repr__())
print(emp1)  # SAME print(emp1.__str__())    # ----> __str__ is running

# print(emp1 + emp2) # can be used for the case of __Add__

print(len(emp2))  # can be used for the method __len__






