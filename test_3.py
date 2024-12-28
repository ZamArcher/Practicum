"""Задача "Шифрованные инструкции".

Марсоход получает с Земли сокращённые инструкции с заданиями, например:
с — сделать снимок;
в — взять образец грунта;
ш — сделать шаг;
о — включить освещение;
и — инициировать сканирование местности.
Из-за ограничений канала связи инструкции отправляются в сжатом виде.
Например, если марсоходу нужно сделать 10 снимков подряд, инструкция будет
выглядеть как 10[с].

Число перед квадратными скобками обозначает, сколько раз надо повторить
последовательность внутри скобок. Скобки могут быть вложенными: 2[ш3[с]]10[с].

Таким образом, командный центр на Земле может отправить марсоходу сжатую строку
инструкций, а марсоход получит и расшифрует её в полную послед-ть команд.

Команды могут обозначаться символами латиницы или кириллицы.

Пример:
Команда: 2[с]3[в]ш
Расшифровка: «ссвввш».
Смысл: сделать два снимка, взять три образца грунта и сделать шаг.

Пример 2:
Команда: 2[в3[ш]]с
Расшифровка: «вшшшвшшшс»
Смысл: Взять образец грунта, сделать три шага; взять образец грунта, сделать
три шага; сделать снимок.

Напишите программу, которая расшифровывает сжатые сообщения и возвращает
строку с командами.

Не забудьте добавить в код аннотации типов данных.

После успешного прохождения тестов на платформе Яндекс Контест отправьте
решение на проверку ревьюеру.

Формат ввода
Сокращенная форма команды. Например, 3[a]2[bc]. Гарантированно приходит
валидная строка. В строке могут быть только буквы, числа и квадратные скобки.

Длина строки может находиться в диапазоне от 0 (пустая строка) до 30 символов
включительно. Числа в строке могут быть от 1 до 300 включительно.

Формат вывода
Полная форма команды. Например, aaabcbc.
"""

# ID посылки 130807014
from typing import List


def decrypt_message(short_msg: str) -> str:
    """Функция расшифровки коротких сообщений."""
    temp_number: str = ''
    numeric_stack: List[tuple] = []
    result: str = ''
    for token in short_msg:
        if token == ']':
            current_msg, number = numeric_stack.pop()
            result = current_msg + number * result
        elif token.isdigit():
            temp_number += token
        elif token == '[':
            numeric_stack.append((result, int(temp_number)))
            temp_number = ''
            result = ''
        else:
            result += token
    return result


if __name__ == '__main__':
    short_msg = input()
    print(decrypt_message(short_msg))

    # test_1 = ''
    # test_2 = '2[a]'
    # test_3 = '3[a]2[bc]'
    # test_4 = '2[abc]3[cd]ef'
    # test_5 = '2[с]3[в]ш'
    # test_6 = '3[a2[c]]'
    # test_7 = '2[в3[ш]]с'

    # assert decrypt_message(test_1) == ''
    # assert decrypt_message(test_2) == 'aa'
    # assert decrypt_message(test_3) == 'aaabcbc'
    # assert decrypt_message(test_4) == 'abcabccdcdcdef'
    # assert decrypt_message(test_5) == 'ссвввш'
    # assert decrypt_message(test_6) == 'accaccacc'
    # assert decrypt_message(test_7) == 'вшшшвшшшс'