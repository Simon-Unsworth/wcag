import unittest
from html_file_dao import HtmlFileDao

class TestHtmlFileDao(unittest.TestCase):
    def setUp(self):
        #Arrange
        self.false_html_path = './fixtures/big.html'
        self.correct_html_path = './fixtures/small.html'
        self.file_dao = HtmlFileDao()
        
        with open(self.correct_html_path, 'r') as html_file:
            self.html_content = html_file.read()

    def test_file_not_found(self):
        #Act
        #Assert
        with self.assertRaises(FileNotFoundError):
            self.file_dao.get_html(self.false_html_path)

    def test_file_found(self):
        #Act
        result = self.file_dao.get_html(self.correct_html_path)
        #Assert
        assert(result)

    def test_assert_correct_content(self):
        #Act
        result = self.file_dao.get_html(self.correct_html_path)
        #Assert
        self.assertEqual(result, self.html_content)