import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), 7)

if __name__ == '__main__':
    unittest.main()
