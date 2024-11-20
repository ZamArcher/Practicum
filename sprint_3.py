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
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
#         self.__discount = 10

#     # Реализуйте методы get_price() и set_discount().
#     def get_price(self, original_price):
#         new_price = round(original_price * (1 - self.__discount / 100), 2)
#         return new_price

#     def set_discount(self, new_discount):
#         if new_discount <= 80:
#             self.__discount = new_discount
#         else:
#             self.__discount = 80


# # Проверим работу программы:
# customer = Customer('Иван Иванович')
# original_price = 85
# print(
#     f'С исходной скидкой Иван Иванович заплатит '
#     f'{customer.get_price(original_price)} рублей вместо {original_price}'
# )
# # Изменим скидку до неприемлемого уровня.
# # Метод set_discount() должен уменьшить размер скидки до 80%.
# customer.set_discount(90)
# print(
#     f'С новой скидкой Иван Иванович заплатит '
#     f'{customer.get_price(original_price)} рублей вместо {original_price}'
# )
# ---------------------
# class Solution:
#     def isValid(self, s: str) -> bool:
#         brackets_pair = {
#             ')': '(',
#             ']': '[',
#             '}': '{',
#         }
#         new_string = 'Z'

#         for char in s:
#             if char in brackets_pair:
#                 if new_string[-1] == brackets_pair[char]:
#                     new_string = new_string[:-1]
#                 else:
#                     return False
#             else:
#                 new_string += char
#         return False if new_string != 'Z' else True


# test = Solution()
# print(test.isValid('()'))
# print(test.isValid('()[]{}'))
# print(test.isValid('(]'))
# print(test.isValid('([])'))
# print(test.isValid('([)]'))
# print(test.isValid('(){}}{'))
# -------------------------
# Импортируйте необходимые модули.
# from typing import List
# from datetime import datetime

# DATE_FORMAT = '%d.%m.%Y'


# # Укажите два параметра функции:
# def validate_record(name, date_of_birth):
#     # Напишите код, верните булево значение.
#     try:
#         date_of_birth = datetime.strptime(date_of_birth, DATE_FORMAT)
#         return True
#     except ValueError:
#         print(f'Некорректный формат даты в записи: {name}, {date_of_birth}')
#         return False


# # Укажите параметры функции:
# def process_people(data: List[tuple]) -> dict:
#     # Объявите счётчики.
#     good_count = bad_count = 0

#     # в каждой паре значений из списка data
#     # проверьте корректность формата даты рождения
#     # и в зависимости от результата проверки увеличьте один из счётчиков.
#     for name, date_of_birth in data:
#         if validate_record(name, date_of_birth):
#             good_count += 1
#         else:
#             bad_count += 1

#     return {'good': good_count, 'bad': bad_count}


# data = [
#     ('Иван Иванов', '10.01.2004'),
#     ('Пётр Петров', '15.03.1956'),
#     ('Зинаида Зеленая', '6 февраля 1997'),
#     ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
#     ('Кирилл Кириллов', '26/11/2003'),
# ]

# # data = [
# #     ('Акакій Башмачкинъ', '23 марта 1791 года'),
# #     ('Яков Степанов', 'Двадцать шестое июля 1971'),
# #     ('Потап Алексеев', '16.09.1990'),
# #     ('Евгений Женин', '5 декабря 1984'),
# #     ('Кондрат Александров', '18.01.1994'),
# # ]

# statistics = process_people(data)
# # Выведите на экран информацию о корректных и некорректных записях
# # в таком формате:
# # Корректных записей: <число>
# # Некорректных записей: <число>

# print('Корректных записей:', statistics['good'])
# print('Корректных записей:', statistics['bad'])

# # Answer
# # Некорректный формат даты в записи: Акакій Башмачкинъ, 23 марта 1791 года
# # Некорректный формат даты в записи: Яков Степанов, Двадцать шестое июля 1971
# # Некорректный формат даты в записи: Евгений Женин, 5 декабря 1984
# # Корректных записей: 2
# # Некорректных записей: 3
# ------------------------------
# from datetime import datetime
# from random import sample


# def choose_days():
#     # Определяем диапазон дат первой половины месяца.
#     first_month_half = list(range(0, 15))

#     # Выбор трёх случайных чисел:
#     random_days = sample(first_month_half, k=3)
#     # Cортировка этих чисел по возрастанию:
#     sorted_days = sorted(random_days)

#     # Получаем сегодняшнюю дату.
#     # На её основе будут генерироваться даты для занятий:
#     now = datetime.now()

#     # Чтобы было проще формировать сообщение, начнём цикл с 1.
#     for i in range(1, 4):
#         # Генерируем дату занятия, подменяя номер дня в сегодняшней дате.
#         practice_day = now.replace(day=sorted_days[i - 1]).strftime("%d.%m.%Y")
#         print(f'{i}-е занятие: {practice_day}')


# choose_days()
# ---------------------------------
# Список для тестирования.
numbers = [1, 4, 11]

# Здесь напишите ваше генераторное выражение.
simple_generator = sum(digit**2 for digit in numbers if digit % 3 == 0)

# Распечатайте сумму квадратов.
print(simple_generator)
