class HtmlFileDao():
    def get_html(self, path):
        with open(path, 'r') as file:
            html = file.read()
            return html