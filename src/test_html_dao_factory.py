import unittest
from html_dao_factory import HtmlDaoFactory
from html_file_dao import HtmlFileDao
from html_http_dao import HtmlHttpDao


class TestHtmlDaoFactory(unittest.TestCase):
    def test_is_url(self):
        self.assertTrue(HtmlDaoFactory.is_url("https://www.google.com"))
    
    def test_is_path(self):
        self.assertFalse(HtmlDaoFactory.is_url("C:\\"))

    def test_makes_http_dao(self):
        self.assertIsInstance(HtmlDaoFactory.make_dao("https://www.google.com"), HtmlHttpDao)
    
    def test_makes_file_dao(self):
        self.assertIsInstance(HtmlDaoFactory.make_dao("C:\\"), HtmlFileDao)
