import unittest 
import random_func

class TestRandomFunc(unittest.TestCase):
    def test_random_func(self):
        self.assertEqual(random_func(5), 10, "random_func(5) should return 10")
