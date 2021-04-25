import unittest

class TestCalculations(unittest.TestCase):

    def test_two_plus_two(self):
        self.assertEqual((2+2),4)

    def test_sum_easy(self):
        self.assertEqual(sum([42, 13, 63]),118)
        self.assertTrue((42+42),84)

    def test_archimedes_pi(self):
        estimates = []
        polygon_sides = [6, 12, 24, 48, 96, 192, 384]
        side_len = 1
        for polygon in polygon_sides:
            side_half = side_len/2
            # Pythagoreanm theorem
            a = (1-(side_half**2))**0.5
            b = 1 - a
            perimeter = polygon * side_len
            estimate_pi = perimeter / 2
            estimates.append(estimate_pi)
            side_len = ((b**2)+(side_half**2))**0.5
        self.assertEqual(estimates[0], 3.0)
        self.assertEqual(estimates[1], 3.105828541230249)
        self.assertEqual(estimates[2], 3.1326286132812378)
        self.assertEqual(estimates[3], 3.1393502030468667)
        self.assertEqual(estimates[4], 3.14103195089051)
        self.assertEqual(estimates[5], 3.1414524722854624)
        self.assertEqual(estimates[6], 3.141557607911858)

    def test_sorting(self):
        lst = [8, 4, 105, 531, 0.1, 419, 9075, 65, 873, 10045, 46021, 1, 0.25, -0.4, -156, 0.12, 1.62, 7.3, 196.32, 419.7]
        lst.sort()
        self.assertEqual(lst, [-156, -0.4, 0.1, 0.12, 0.25, 1, 1.62, 4, 7.3, 8, 65, 105, 196.32, 419, 419.7, 531, 873, 9075, 10045, 46021])
        self.assertEqual(sum(lst), 67616.01000000001)

if __name__ == '__main__':
    unittest.main()
