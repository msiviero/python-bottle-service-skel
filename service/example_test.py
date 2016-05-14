import unittest

import service.example


class TestStringMethods(unittest.TestCase):
    def test_greet(self):
        expected = 'World'
        result = service.example.C.greet('World')

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
