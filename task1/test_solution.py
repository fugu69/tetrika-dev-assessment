import unittest
from functools import partial

# Импорт декоратора strict
from solution import strict  # Замени 'solution' на имя своего файла без .py

class TestStrictDecorator(unittest.TestCase):

    def test_correct_types(self):
        @strict
        def add(a: int, b: int) -> int:
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_type_error_single_argument(self):
        @strict
        def square(x: int) -> int:
            return x * x

        with self.assertRaises(TypeError) as cm:
            square("не число")
        self.assertIn("Аргумент 'x' должен быть типа int", str(cm.exception))

    def test_type_error_multiple_arguments(self):
        @strict
        def concat(a: str, b: str) -> str:
            return a + b

        with self.assertRaises(TypeError) as cm:
            concat("hello", 42)
        self.assertIn("Аргумент 'b' должен быть типа str", str(cm.exception))

    def test_missing_annotations_are_ignored(self):
        @strict
        def func(a, b: int):
            return b

        # Ошибки не будет, потому что параметр 'a' не имеет аннотации
        self.assertEqual(func("любой тип", 10), 10)

    def test_kwargs_are_ignored(self):
        @strict
        def greet(name: str, **kwargs):
            return f"Привет, {name}!"

        self.assertEqual(greet("Макс", неиспользуемый_параметр="игнор"), "Привет, Макс!")

    def test_partial_function_support(self):
        @strict
        def multiply(a: int, b: int):
            return a * b

        part = partial(multiply, "ошибка")  # Первый аргумент — не int

        with self.assertRaises(TypeError):
            part(5)

    def test_no_annotations(self):
        @strict
        def nothing(a, b):
            return True  # Возвращает просто True, не вызывает ошибок типов

        self.assertTrue(nothing(1, "строка"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
