import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('job-distribution scheme'.upper(), 'JOB-DISTRIBUTION SCHEME')
        self.assertTrue('BROKER'.isupper())
        self.assertFalse('Implementation'.isupper())

    def test_split(self):
        sentence = "Welcome to this test"
        self.assertEqual(sentence.split(),["Welcome","to","this","test"])

if __name__ == '__main__':
    unittest.main()
