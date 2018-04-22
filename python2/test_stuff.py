import unittest


class SomeTest(unittest.TestCase):
    def test_it(self):
        print "this is some test"

        self.assertEqual(True, 1 == 1)
