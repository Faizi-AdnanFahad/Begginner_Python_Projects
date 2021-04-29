class Employee:

    @property
    def get_full_name(self):
        return self._get_full_name

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # with this we can access this method without declaring parenthesis, e.g., --> self.get_email
    # without it, we would get the object location in the memory
    def get_email(self):
        return f"{self.first.capitalize()}.{self.last.capitalize()}@email.com"

    @property  # acts like getter
    def get_full_name(self):
        return f"{self.first.capitalize()} {self.last.capitalize()}"

    @get_full_name.setter  # acts like setters
    def get_full_name(self, new_name):
        self.first, self.last = new_name.split(' ')

    @get_full_name.deleter  # acts like setters
    def get_full_name(self, new_name):
        print('Delete Name!')
        self.first = None
        self.last


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.get_full_name)

del emp_1.get_full_name
print(emp_1.first)

#
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.get_full_name)  # print(emp_1.get_full_name) because of @property
#
# # because of @get_full_name.setter
# # we can set a new value for attributes










