import inspect
import unittest


def strict(func):
    def wrapper(*args):
        sig = inspect.signature(func)
        for val, (name, param) in zip(args, sig.parameters.items()):
            expected_type = param.annotation
            if not isinstance(val, expected_type):
                raise TypeError(
                    f"Argument '{name}' must be {expected_type.__name__}, got {type(val).__name__}"
                )
        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


class StrictTestCase(unittest.TestCase):

    def test_strict_valid(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_strict_invalid(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
