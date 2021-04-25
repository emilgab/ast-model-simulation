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

if __name__ == '__main__':
    unittest.main()
