from utils import get_greeting, get_max_number, multiply_numbers

def main() -> None:
    print(get_greeting())
    print(get_max_number([1, 5, "a", 2.5]))
    print(multiply_numbers(3, 4))


if __name__ == "__main__":
    main()