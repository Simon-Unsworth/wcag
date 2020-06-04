import unittest
from html_http_dao import HtmlHttpDao
import requests
import urllib3.exceptions

class TestHtmlHttpDao(unittest.TestCase):
    def setUp(self):
        #Arrange
        self.false_html_url = 'https://www.thisisanincorrecturl.com/'
        self.correct_html_url = 'https://en.wikipedia.org/wiki/Doom_(1993_video_game)'
        self.http_dao = HtmlHttpDao()

    def test_url_not_found(self):
        #Act
        html = self.http_dao.get_html(self.false_html_url)
        
        #Assert
        self.assertEqual(None, html)


    def test_url_found(self):
        #Act
        result = self.http_dao.get_html(self.correct_html_url)
        
        #Assert
        assert(result)

    def test_assert_correct_content(self):
        #Act
        self.html_content = requests.get('https://en.wikipedia.org/wiki/Doom_(1993_video_game)').text
        result = self.http_dao.get_html(self.correct_html_url)

        #Assert
        self.assertEqual(result, self.html_content)