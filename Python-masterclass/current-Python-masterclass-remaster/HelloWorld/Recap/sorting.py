# # list = [9, 5, 2, 1, 5, 3]
# # sorted_list = sorted(list)  # creates a new list and sorts it ascending order
# # # sorted_list = sorted(list, reverse=True)  # creates a new list and sorts it descending order
# #
# # print(f"original list: {list}")
# # print(f"sorted list: {sorted_list}")
# #
# # a = {1: 'one', 2: 'two', 3: 'three'}
#
#
# # SORTING BASED ON A SPECIFIC CONDITION
#
# class obj:
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def __repr__(self):
#         return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
#
#
# e1 = obj("Ahmad", 20, 1000)
# e2 = obj("Mahmoud", 22, 3000)
# e3 = obj("Salim", 25, 400)
#
# list_of_objects = [e1, e2, e3]
#
#
# # sorted_list_of_objects = sorted(list_of_objects)  # this will cause an error
#
#
# def sort_according_to_object_names(emp):
#     return emp.name
#
#
# def sort_according_to_object_age(emp):
#     return emp.age
#
#
# def sort_according_to_object_salary(emp):
#     return emp.salary
#
#
# sorted_based_on_names = sorted(list_of_objects, key=sort_according_to_object_names)
# print(sorted_based_on_names)
#
# sorted_based_on_age = sorted(list_of_objects, key=sort_according_to_object_age)
# print(sorted_based_on_names)
#
# sorted_based_on_salary = sorted(list_of_objects, key=sort_according_to_object_salary)
# print(sorted_based_on_names)








a = ['234', 'aklsdjflkashlfashijkdfhajklhfd', 'dslkfadsafadfsa']

def sorted_based_on_length(list):
    return len(list)

sorted_based_on_len_of_element_char = sorted(a, key=sorted_based_on_length)
print(sorted_based_on_len_of_element_char)









