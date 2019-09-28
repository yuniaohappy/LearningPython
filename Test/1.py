import unittest

class TestStrMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            print(s.split(5))

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()