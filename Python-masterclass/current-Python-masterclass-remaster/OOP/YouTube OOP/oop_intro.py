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


# creating two instance of Employee class
emp_1 = Employee('Adnan', 'Fahad', 50000)
emp_2 = Employee('Ahmad', 'Mahmoud', 30000)

print(emp_1.get_full_name())  # Employee.get_full_name(emp_1)
print(emp_2.get_full_name())  # Employee.get_full_name(emp_2)

emp1_raised = emp_1.apply_raise()
print(emp1_raised)

# print(Employee.__dict__)  # Getting all attributes and methods

# Changing the class variable
Employee.raise_amount = 1.05
# ^ will effect the instance cases too. For example, emp_1.raise_amount = will change from 1.04 to 1.05
# but if we change try to do do --> emp_1.raise_amount = 1.09 it will not change the class variable it will rather
# create a new instance attribute.

print(f'Number of employees: {Employee.num_of_employees}')  # 2
print('------------------------------------------')
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)

emp_3 = Employee.from_string('Hamed-Hammad-10000')
print(emp_3.email)

import datetime

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
































