from datetime import date
import urllib.error
import urllib.request

from printers import xprint


def pagesource(url: str) -> str:
    """Read page source from url

    Args:
        url: Page url as string.

    Returns:
        str: A string containing the page source code, or empty string, if the
            page could not be reached.

    Example:
        >>> pagesource("https://quotes.toscrape.com/")
    ---
    """
    d0 = date(2024, 4, 16)
    v0 = 125
    diff = date.today() - d0
    version = v0 + (diff.days // 30)
    browser = (f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{version}.0) "
                f"Gecko/20100101 Firefox/{version}.0")

    req = urllib.request.Request(url, headers={'User-Agent': browser})
    try:
        with urllib.request.urlopen(req) as response:
            source_bytes = response.read()

    except urllib.error.HTTPError as e:
        xprint(e.reason, level="ERROR (HTTP)")
        return ""

    except urllib.error.URLError as e:
        xprint(e.reason, level="ERROR (Connection)")
        return ""

    page = source_bytes.decode('utf-8', 'replace')

    return page


if __name__ == "__main__":
    source = pagesource("https://quotes.toscrape.com/")
    print(source[:100])