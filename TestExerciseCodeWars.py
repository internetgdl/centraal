import unittest
import Exercise1CodeWars

class TestExerciseCodeWares(unittest.TestCase):

    def test_product(self):
        self.assertEqual(Exercise1CodeWars.longest_consec(["it","it","it", "it", "it","iti"], 6), "ititititititi")
	self.assertSetEqual(Exercise1CodeWars.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertSetEqual(Exercise1CodeWars.longest_consec([], 3), "")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertSetEqual(Exercise1CodeWars.longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

if __name__ == '__main__':
    suite =  unittest.TestLoader().loadTestsFromTestCase(TestExerciseCodeWares)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
