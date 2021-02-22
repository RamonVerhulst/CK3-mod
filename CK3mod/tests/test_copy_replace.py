from os import remove
from unittest import TestCase

from CK3mod.copy_replace import main

text = '''
cultural_names = {
    pictish = cn_pictavia
    irish = cn_alba
    gaelic = cn_alba
}
'''
expected = '''
cultural_names = {
    pictish = cn_pictavia
    irish = cn_alba
    gaelic = cn_alba
    welsh = cn_alba
}
'''


class TestMain(TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        remove('sample.txt')

    def test_gaelic_welsh(self):
        with open('sample.txt', 'w') as f:
            f.write(text)

        main('sample.txt', 'gaelic', 'welsh')

        with open('sample.txt') as f:
            actual = f.read()
            self.assertEqual(expected, actual)

    def test_foo(self):
        self.assertTrue(True)
