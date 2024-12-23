"""Задача "Обойди дерево".

В прекоде к заданию описано дерево. Каждый узел дерева — это объект класса
Spaceman. У этого класса:
два обязательных атрибута — name и space_experience;
два опциональных атрибута — father и mother, эти атрибуты заполняются,
если родители космонавта тоже были космонавтами.
В коде дана заготовка функции count_dynasty_experience. Допишите её так,
чтобы при передаче в неё объекта класса Spaceman, функция посчитала
«марсианский стаж» космонавта и всех его предков.
Решением должен быть рекурсивный обход дерева: в каждом следующем уровне
рекурсии должны обрабатываться узлы, хранящиеся в атрибутах father и mother
текущего узла.

При решении никаких новых классов и функций создавать не надо, всё должно
происходить внутри count_dynasty_experience.
"""

from __future__ import annotations
from typing import Optional


class Spaceman:
    """Класс принадлежности к космонафтам."""

    def __init__(
        self,
        name: str,
        space_experience: int,
        father: Optional[Spaceman] = None,
        mother: Optional[Spaceman] = None,
    ):
        """Инициализация объекта класса Spaceman."""
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


def count_dynasty_experience(spaceman: Spaceman) -> int:
    """Функция высчитывает "марсианский стаж" космонафта и всех его предков."""
    total_experience = 0
    # Доработайте функцию, чтобы она считала
    # суммарный опыт династии космонавтов.
    total_experience += spaceman.space_experience
    if spaceman.father:
        total_experience += count_dynasty_experience(spaceman.father)
    if spaceman.mother:
        total_experience += count_dynasty_experience(spaceman.mother)
    return total_experience


yu_a_tatarin = Spaceman(
    name='Юрий Алексеевич Татарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Татарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева', space_experience=1
        ),
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5),
)
result = count_dynasty_experience(yu_a_tatarin)
print(result)
