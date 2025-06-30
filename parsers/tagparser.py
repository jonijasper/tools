"""
HTML Parser template module

Example usage:
    from tagparser import TagParser

    with open("html_doc.html", 'r') as f:
        html_str = f.read()

    parser = TagParser()
    parser.feed(html_str)
    parser.close()
"""
from html.parser import HTMLParser

class TagParser(HTMLParser):
    """Find and handle html tags

    Inherits from html.parser.HTMLParser

    Methods:
        handle_starttag: <tag>
        handle_startendtag: <tag />
        handle_data: > data </
        handle_endtag: </tag>
        handle_comment: <!--comment-->

    Usage:
        parser = TagParser()
        parser.feed(html_str)
        parser.close()

    """
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attr):
        pass

    def handle_startendtag(self, tag, attr):
        pass

    def handle_data(self, data):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_comment(self, comment):
        pass

if __name__ == "__main__":
    print(f"\N{goat}")