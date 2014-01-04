import markgen
from six import string_types
from bs4 import BeautifulSoup


def markup_to_markdown(content):
    soup = BeautifulSoup(content)

    # Account for HTML snippets and full documents alike
    contents = soup.body.contents if soup.body is not None else soup.contents

    return _iterate_over_contents(contents)


def _iterate_over_contents(contents):
    out = u''

    for c in contents:
        if not isinstance(c, string_types):
            c = _iterate_over_contents(c)

        out += u"\n{0}".format(c)

    return out
