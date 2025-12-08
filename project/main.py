from unittest import result
from test_ import run_library_demo
from book_library import Book, Library
from typing import TypeVar
import pytest
from typing import Callable, Any, Dict
from utils import (
    get_ticket_price,
    greet_person,
    is_even,
    reverse_string,
    calculate_average,
    add_person_to_list,
    count_vowels,
    fahrenheit_to_celsius,
)



def main():
    print(f"Результат (за замовчуванням): {greet_person()}")
    print(f"Результат (з ім'ям): {greet_person('Богдан')}")


    print(f"12 парне? {is_even(12)}")
    print(f"13 парне? {is_even(13)}")


    text = "Навчання"
    print(f"Оригінал: '{text}' -> Реверс: '{reverse_string(text)}'")

    nums = [10.0, 20.0, 30.0]
    print(f"Середнє для {nums}: {calculate_average(nums)}")


    original = ["Олег", "Ірина"]
    print(f"Оригінал (до): {original}")

    новий_список = add_person_to_list(original, "Дмитро")

    print(f"Оновлений список: {новий_список}")
    print(f"Оригінал після: {original} Не змінився")


    vowel_text = "Привіт, світ"
    print(f"Голосні у '{vowel_text}': {count_vowels(vowel_text)}")


    temp_f = 86.0
    print(f"{temp_f}°F = {fahrenheit_to_celsius(temp_f)}°C")


if __name__ == '__main__':
    run_library_demo()


