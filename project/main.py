from unittest import result
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


def run_ticket_price_tests():


    while True:
        try:
            age_input = input("Введіть скільки вам років: ")

            age = int(age_input)

            if age < 0:
                print("Вік не може бути від'ємним. Спробуйте ще раз.")
                continue

            break

        except ValueError:
            print("Це не число. Будь ласка, введіть вік цифрами.")


    final_price = get_ticket_price(age)



    print(f"Кінцева вартість: {final_price:.2f} грн")



@pytest.mark.parametrize(
    "age, expected_price",
    [
        (0, 0.0),
        (5, 0.0),

        (6, 50.0),
        (10, 50.0),
        (17, 50.0),

        (18, 100.0),
        (45, 100.0),
        (59, 100.0),

        (60, 70.0),
        (90, 70.0),

        (-5, 0.0),
    ]
)

def test_get_ticket_price_boundaries(age: int, expected_price: float):
    actual_price = get_ticket_price(age)

    assert round(actual_price, 2) == round(expected_price, 2)





def wrap_in_dict(func: Callable) -> Callable:


    def wrapper(*args: Any, **kwargs: Any) -> Dict[str, Any]:
        function_result = func(*args, **kwargs)


        return {"result": function_result}


    return wrapper



@wrap_in_dict
def calculate_sum(a: int, b: int) -> int:

    return a + b


sum_result = calculate_sum(10, 5)
print(f"Результат виклику calculate_sum(10, 5): {sum_result}")
print(f"Тип результату: {type(sum_result)}")



@wrap_in_dict
def get_status() -> str:

    return "Операція успішна"



status_result = get_status()
print(f"Результат виклику get_status(): {status_result}")




R = TypeVar('R')


def round_result(ndigits: int) -> Callable[[Callable[..., R]], Callable[..., R]]:


    def decorator(func: Callable[..., R]) -> Callable[..., R]:


        def wrapper(*args: Any, **kwargs: Any) -> R:

            if isinstance(result, (int, float)):
                return round(result, ndigits)
            else:

                return result

        return wrapper

    return decorator


@round_result(ndigits=2)
def divide_numbers(a: int, b: int) -> float:
    return a / b



result_1 = divide_numbers(10, 3)
print(f"Результат divide_numbers(10, 3): {result_1} (Тип: {type(result_1)})")


@round_result(ndigits=0)
def calculate_area(radius: float) -> float:
    import math
    return math.pi * (radius ** 2)


result_2 = calculate_area(2)
print(f"Результат calculate_area(2): {result_2} (Тип: {type(result_2)})")



@round_result(ndigits=3)
def get_user_data(name: str) -> dict:

    return {"name": name, "score": 98.7654321}


result_3 = get_user_data("Alex")
print(f"Результат get_user_data('Alex'): {result_3} (Тип: {type(result_3)})")





def run_library_demo():

    book_a = Book(author="Джордж Орвелл", title="1984")
    book_b = Book(author="Тарас Шевченко", title="Кобзар")
    book_c = Book(author="Рей Бредбері", title="451° за Фаренгейтом")


    id_for_removal = book_a.id
    print(f"Створено книгу '{book_a.title}'. Її ID для видалення: {id_for_removal[:8]}...")


    main_library = Library("Міська Центральна Бібліотека")

    main_library.add_book(book_a)
    main_library.add_book(book_b)
    main_library.add_book(book_c)

    main_library.display_books()

    main_library.remove_book(id_for_removal)

    main_library.remove_book("неіснуючий-id-123")

    main_library.display_books()


if __name__ == '__main__':
    run_library_demo()


