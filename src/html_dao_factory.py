from html_file_dao import HtmlFileDao
from html_http_dao import HtmlHttpDao


class HtmlDaoFactory():
    @staticmethod
    def make_dao(resouce):
        return HtmlHttpDao() if HtmlDaoFactory.is_url(resouce) else HtmlFileDao()

    @staticmethod
    def is_url(resource):
        return resource[:4] == 'http'