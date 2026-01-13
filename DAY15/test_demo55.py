import unittest

class test_myclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = 10
        cls.b = 20
        print('Called/Invoked Once before any tests in class')

    def test_method1(self):
        result = self.a + self.b
        self.assertTrue(result==300)
    @classmethod    
    def tearDownClass(cls):
        print("end of the testcase")
    def setUp(self):
        self.a = 100
        self.b = 200
        
if __name__ == '__main__':
    unittest.main()