import unittest
import functions

class TestFunctions(unittest.TestCase):

    def test_product(self):
        self.assertSetEqual(functions.add_by(5,5),'25')

if __name__ == '__main__':
    suite =  unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=0).run(suite)
    