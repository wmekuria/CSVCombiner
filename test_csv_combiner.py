import unittest
from csv_combiner import FileCombiner
from unittest import mock
from unittest.mock import patch
import io

class TestFileCombiner(unittest.TestCase):

    def setUp(self):
        self.combiner = FileCombiner()
        self.combiner_2 = FileCombiner(False)

    def test_filetype(self):
        dummy_files = 'clothing.txt'
        with self.assertRaises(TypeError):
            self.combiner.display_csv(dummy_files)

    def test_header(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as header_stdout_1:
            self.combiner.display_header()
        with mock.patch('sys.stdout', new=io.StringIO()) as header_stdout_2:
            self.combiner_2.display_header()

        self.assertEqual(header_stdout_1.getvalue(), '"email_hash","category","filename"\n')
        self.assertEqual(header_stdout_2.getvalue(), '"email_hash","category"\n')
    def test_combiner (self):
        dummy_string = 'clothing.txt'
        with self.assertRaises(TypeError):
            self.combiner.display_combined(dummy_string)



if __name__ == '__main__':
    unittest.main()