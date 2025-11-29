import pytest
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


if __name__ == '__main__':
    run_ticket_price_tests()

