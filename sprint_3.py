# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# class Solution:
#     def isValid(self, s: str) -> bool:
#         round_bracket = square_bracket = curly_bracket = 0
#         for char in s:
#             if char == '(':
#                 round_bracket += 1
#             elif char == ')':
#                 round_bracket -= 1
#             elif char == '[':
#                 square_bracket += 1
#             elif char == ']':
#                 square_bracket -= 1
#             elif char == '{':
#                 curly_bracket += 1
#             elif char == '}':
#                 curly_bracket -= 1
#             if round_bracket < 0 or square_bracket < 0 or curly_bracket < 0:
#                 return False

#         if round_bracket == square_bracket == curly_bracket == 0:
#             return True
#         else:
#             return False


# test_string = Solution()
# print(test_string.isValid("()"))
# print(test_string.isValid("()[]{}"))
# print(test_string.isValid("(]"))
# print(test_string.isValid("([)]"))
# print(test_string.isValid("(([])"))
# ---------------------------
# class Employee:
#     vacation_days = 28

#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days

#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days

#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


# # Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.
# class FullTimeEmployee(Employee):

#     def __init__(self, first_name, second_name, gender):
#         super().__init__(first_name, second_name, gender)
#         self.remaining_vacation_days = FullTimeEmployee.vacation_days

#     def get_unpaid_vacation(self, start_date: str, days: int) -> str:
#         return (
#             f'Начало неоплачиваемого отпуска: {start_date}, '
#             f'продолжительность: {days} дней.'
#         )


# class PartTimeEmployee(Employee):
#     vacation_days = 14

#     def __init__(self, first_name, second_name, gender):
#         super().__init__(first_name, second_name, gender)
#         self.remaining_vacation_days = PartTimeEmployee.vacation_days

#     # def __init__(self, dial_type_value, network_type):
#     #     super().__init__(remaining_vacation_days)


# # Пример использования:
# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
# print(part_time_employee.get_vacation_details())
# ----------------------------
class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id()

    def __generate_employee_id(self):
        return hash(self.first_name + self.second_name + self.gender)

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):

    def __init__(self, first_name, second_name, gender, __salary):
        super().__init__(first_name, second_name, gender)
        self.__salary = __salary

    def __get_vacation_salary(self):
        return 0.8 * self.__salary

    def get_unpaid_vacation(self, start_date, days):
        return (
            f'Начало неоплачиваемого отпуска: {start_date}, '
            f'продолжительность: {days} дней.'
        )


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# Пример использования:
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())

# print(full_time_employee._Employee__get_vacation_salary())
