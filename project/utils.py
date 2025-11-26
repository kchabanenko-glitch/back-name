from typing import List, Union
import logging


logger = logging.getLogger("project_logger")


def greet_person(name: str = "Гість") -> str:

    print(f"[LOG]: Створюю привітання для '{name}'.")
    return f"Привіт, {name}!"




def is_even(number: int) -> bool:

    result = number % 2 == 0
    print(f"[LOG]: Перевіряю {number}. Парне? {result}.")
    return result




def reverse_string(text: str) -> str:

    reversed_text = text[::-1]
    print(f"[LOG]: Обертаю рядок.")
    return reversed_text




def calculate_average(numbers: list) -> float:

    if not numbers:
        print("[LOG]: Список порожній, повертаю 0.0.")
        return 0.0

    average = sum(numbers) / len(numbers)
    print(f"[LOG]: Обчислено середнє: {average}.")
    return average




def add_person_to_list(people: list, person: str) -> list:

    new_people_list = people[:]
    new_people_list.append(person)

    print(f"[LOG]: Додано '{person}'. Оригінал не змінений.")
    return new_people_list




def count_vowels(text: str) -> int:

    vowels = "aeiouyаеєиіїоуюя"
    text_lower = text.lower()


    count = 0
    for char in text_lower:
        if char in vowels:
            count += 1

    print(f"[LOG]: Підраховано {count} голосних.")
    return count




def fahrenheit_to_celsius(f: float) -> float:
    c = (f - 32.0) * (5.0 / 9.0)
    print(f"[LOG]: Конвертовано {f}°F у {c}°C.")
    return c




