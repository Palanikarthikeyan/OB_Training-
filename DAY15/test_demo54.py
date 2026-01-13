import unittest

class test_myclass(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        
    def test_method1(self):
        result = self.a + self.b
        self.assertTrue(result==300)
        
    def tearDown(self):
        print("end of the testcase")
        
if __name__ == '__main__':
    unittest.main()