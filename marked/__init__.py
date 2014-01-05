import markgen
from bs4 import BeautifulSoup

TAGS = {
    'p': 'paragraph',
    'div': 'paragraph',
    'a': 'link',
    'strong': 'emphasis',
    'em': 'emphasis',
    'b': 'emphasis',
    'i': 'emphasis',
    'u': 'emphasis',
    'img': 'image',
    'image': 'image',
    'blockquote': 'quote',
    'pre': 'pre',
    'code': 'pre',
    'h1': 'header',
    'h2': 'header',
    'h3': 'header',
    'h4': 'header',
    'h5': 'header',
    'h6': 'header',
    'ul': 'ulist',
    'ol': 'olist'
}

def markup_to_markdown(content):
    soup = BeautifulSoup(content)

    # Account for HTML snippets and full documents alike
    contents = soup.body.contents if soup.body is not None else soup.contents

    return _iterate_over_contents(contents)


def _iterate_over_contents(contents):
    out = u''

    for c in contents:
        if hasattr(c, 'contents'):
            c.string = _iterate_over_contents(c.contents)

        if c.name in TAGS:
            wrap = getattr(markgen, TAGS[c.name])
            c = wrap(c.string)

        out += u"\n{0}".format(c)

    return out
