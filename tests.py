from unittest import TestCase

def add(a: int, b: int) -> int:
    return a + b


class AppTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
