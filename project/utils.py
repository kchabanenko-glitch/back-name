from typing import List, Union
import logging


logger = logging.getLogger("project_logger")


def get_greeting() -> str:
    logger.info('get_greeting() was called with no arguments')
    return "Hello, buddy"


def get_max_number(values: List[Union[int, float, str, bool]]) -> float:
    logger.info(f'get_max_number() was called with arguments: values={values}')
    numeric_values = [v for v in values if isinstance(v, (int, float))]

    if not numeric_values:
        return 0

    return max(numeric_values)


def multiply_numbers(a: float, b: float) -> float:
    logger.info(f'multiply_numbers() was called with arguments: a={a}, b={b}')
    return a * b

