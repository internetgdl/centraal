import unittest
import Class2_Kata2

class TestExerciseCodeWares(unittest.TestCase):
    def test_product(self):
        self.assertEqual(Class2_Kata2.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(Class2_Kata2.longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(Class2_Kata2.longest_consec([], 3), "")
        self.assertEqual(Class2_Kata2.longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(Class2_Kata2.longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(Class2_Kata2.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(Class2_Kata2.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(Class2_Kata2.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(Class2_Kata2.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

if __name__ == '__main__':
    suite =  unittest.TestLoader().loadTestsFromTestCase(TestExerciseCodeWares)
    unittest.TextTestRunner(verbosity=2).run(suite)
    