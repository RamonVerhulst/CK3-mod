from os import remove
from unittest import TestCase

from CK3mod.delete_2 import main

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
    gaelic = cn_alba
}
'''


class TestMain(TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        remove('sample.txt')

    def test_remove_irish_cn_alba(self):
        with open('sample.txt', 'w') as f:
            f.write(text)

        main('sample.txt', 'irish', 'cn_alba')

        with open('sample.txt') as f:
            actual = f.read()
            self.assertEqual(expected, actual)

    def test_remove_cn_alba_irish(self):
        """Order should not matter"""
        with open('sample.txt', 'w') as f:
            f.write(text)

        main('sample.txt', 'cn_alba', 'irish')

        with open('sample.txt') as f:
            actual = f.read()
            self.assertEqual(expected, actual)

    def should_not_remove_anything(self):
        with open('sample.txt', 'w') as f:
            f.write(text)

        # cn_alba is surely matched, but "dogs" not
        main('sample.txt', 'cn_alba', 'dogs')

        with open('sample.txt') as f:
            actual = f.read()
            self.assertEqual(expected, actual)
