import unittest

class TestIO(unittest.TestCase):

    def test_wine(self):
        wine_amount = 0
        alc_total = 0
        with open("testfiles/wine.csv","r") as wine:
            for row in wine.readlines()[1:]:
                wine_amount += 1
                split_row = row.split(",")
                alc_total += float(split_row[1])
        self.assertEqual(alc_total/wine_amount,13.000617977528083)

    def test_pokerhands(self):
        three_of_a_kind = 0
        royals = 0
        with open("testfiles/poker-hand-training-true.csv") as hands:
            for row in hands.readlines():
                split_row = row.split(",")
                if split_row[-1][0] == "9":
                    royals += 1
                elif split_row[-1][0] == "3":
                    three_of_a_kind += 1
        self.assertEqual(royals,5)
        self.assertEqual(three_of_a_kind,513)

if __name__ == '__main__':
    unittest.main()
