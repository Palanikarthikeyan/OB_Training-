import unittest
from demo53 import calc_add

class Test_demo53_code(unittest.TestCase):
	def test_calc_add(self):
		self.assertEqual(calc_add(3,5),8)
		self.assertEqual(calc_add(4,5),9)


if __name__ == '__main__':
	unittest.main()

