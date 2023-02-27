import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_null_input(self):
        self.assertIsNone(english_to_french(None))

    def test_french_to_english_null_input(self):
        self.assertIsNone(french_to_english(None))

    def test_english_to_french_translation_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english_translation_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_translation_empty_string(self):
        self.assertEqual(english_to_french(''), '')

    def test_french_to_english_translation_empty_string(self):
        self.assertEqual(french_to_english(''), '')

if __name__ == '__main__':
    unittest.main()
