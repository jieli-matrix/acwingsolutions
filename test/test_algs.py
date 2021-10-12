from acwing.algs import power
import unittest

class TestAlgs(unittest.TestCase):
    def test_algs(self):
        for (a, b, p) in (
            (2, 3, 3), (3, 7, 4), (123456789, 0, 1)):
            self.assertEqual(pow(a, b) % p, power(a, b, p))

if __name__ == '__main__':
    unittest.main()