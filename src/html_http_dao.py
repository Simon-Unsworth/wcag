import requests


class HtmlHttpDao():
    def get_html(self, url):
        try:
            html = requests.get(url,timeout=3)
            html.raise_for_status()
            return html.text
        except requests.exceptions.RequestException as err:
            print ("Html Http Dao Fatal Error:", err)
        except requests.exceptions.HTTPError as errh:
            print ("Html Http Dao Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Html Http Dao Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print ("Html Http Dao Timeout Error:", errt)

