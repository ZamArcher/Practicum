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
# class Employee:
#     vacation_days = 28

#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days
#         self._employee_id = self.__generate_employee_id()

#     def __generate_employee_id(self):
#         return hash(self.first_name + self.second_name + self.gender)

#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days

#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


# class FullTimeEmployee(Employee):

#     def __init__(self, first_name, second_name, gender, __salary):
#         super().__init__(first_name, second_name, gender)
#         self.__salary = __salary

#     def __get_vacation_salary(self):
#         return 0.8 * self.__salary

#     def get_unpaid_vacation(self, start_date, days):
#         return (
#             f'Начало неоплачиваемого отпуска: {start_date}, '
#             f'продолжительность: {days} дней.'
#         )


# class PartTimeEmployee(Employee):
#     vacation_days = 14

#     def __init__(self, first_name, second_name, gender):
#         super().__init__(first_name, second_name, gender)
#         self.remaining_vacation_days = PartTimeEmployee.vacation_days


# # Пример использования:
# full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))


# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())
# -------------------------------
# class Product:
#     # Опишите инициализатор класса и метод get_info()
#     def __init__(self, product_name, product_count) -> None:
#         self.product_name = product_name
#         self.product_count = product_count

#     def get_info(self) -> str:
#         return f'{self.product_name} (в наличии: {self.product_count})'


# class Kettlebell(Product):
#     # Опишите инициализитор класса и метод get_weight()

#     def __init__(self, product_name, product_count, weight) -> None:
#         super().__init__(product_name, product_count)
#         self.weight = weight

#     def get_weight(self):
#         return self.get_info() + f'. Вес: {self.weight} кг'


# class Clothing(Product):
#     # Опишите инициализатор класса и метод get_size()

#     def __init__(self, product_name, product_count, size) -> None:
#         super().__init__(product_name, product_count)
#         self.size = size

#     def get_size(self):
#         return self.get_info() + f'. Размер: {self.size}'


# # Для проверки вашего кода создадим пару объектов
# # и вызовем их методы:
# small_kettlebell = Kettlebell('Гиря малая', 15, 2)
# shirt = Clothing('Футболка', 5, 'L')

# print(small_kettlebell.get_weight())
# print(shirt.get_size())
# ----------------------------
# Импортируйте нужную библиотеку.


# from datetime import datetime


# class Store:

#     def __init__(self, address):
#         self.address = address

#     def is_open(self, date):
#         # Метод is_open() в родительском классе всегда возвращает False,
#         # это "код-заглушка", метод, предназначенный для переопределения
#         # в дочерних классах.
#         return False

#     def get_info(self, date_str):
#         # С помощью шаблона даты преобразуйте строку date_str в объект даты:
#         date_object = datetime.strptime(date_str, '%d.%m.%Y')

#         # Передайте в метод is_open() объект даты date_object и определите,
#         # работает ли магазин в указанную дату.
#         # В зависимости от результата будет выбрано значение
#         # для переменной info.
#         if self.is_open(date_object):
#             info = 'работает'
#         else:
#             info = 'не работает'
#         return f'Магазин по адресу {self.address} {date_str} {info}'


# class MiniStore(Store):
#     # Переопределите метод is_open().
#     def is_open(self, date):
#         return True if date.weekday() in [0, 1, 2, 3, 4] else False


# class WeekendStore(Store):
#     # Переопределите метод is_open().
#     def is_open(self, date):
#         return True if date.weekday() in [5, 6] else False


# class NonStopStore(Store):
#     # Переопределите метод is_open().
#     def is_open(self, date):
#         return True


# mini_store = MiniStore('Улица Немига, 57')
# print(mini_store.get_info('29.03.2024'))
# print(mini_store.get_info('30.03.2024'))

# weekend_store = WeekendStore('Улица Толе би, 321')
# print(weekend_store.get_info('29.03.2024'))
# print(weekend_store.get_info('30.03.2024'))


# non_stop_store = NonStopStore('Улица Арбат, 60')
# print(non_stop_store.get_info('29.03.2024'))
# print(non_stop_store.get_info('30.03.2024'))
# ---------------------------------
class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, original_price):
        new_price = round(original_price * (1 - self.__discount / 100), 2)
        return new_price

    def set_discount(self, new_discount):
        if new_discount <= 80:
            self.__discount = new_discount
        else:
            self.__discount = 80


# Проверим работу программы:
customer = Customer('Иван Иванович')
original_price = 85
print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен уменьшить размер скидки до 80%.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
