import unittest 
import random_func

class TestRandomFunc(unittest.TestCase):
    def test_random_func(self):
        for num in [5,10,15]:
            with self.subTest(num=num):
                self.assertEqual(random_func.random_func(num), num+5, "random_func({}) should return {}".format(num,num+5))

if __name__ == '__main__':
    unittest.main()