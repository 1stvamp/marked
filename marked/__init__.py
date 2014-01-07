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
    'code': 'inline_pre',
    'h1': 'header',
    'h2': 'header',
    'h3': 'header',
    'h4': 'header',
    'h5': 'header',
    'h6': 'header',
    'ul': 'ulist',
    'ol': 'olist'
}

ATTRS = {
    'a': {
        'href': 'address',
        'title': 'title'
    },
    'img': {
        'src': 'address',
        'title': 'title'
    },
    'image': {
        'src': 'address',
        'title': 'title'
    }
}

LISTS = [
    'ul',
    'ol'
]

def markup_to_markdown(content):
    soup = BeautifulSoup(content)

    # Account for HTML snippets and full documents alike
    contents = soup.body.contents if soup.body is not None else soup.contents

    return _iterate_over_contents(contents)


def _iterate_over_contents(contents):
    out = u''

    for c in contents:
        if hasattr(c, 'contents'):
            c.string.replace_with(_iterate_over_contents(c.contents))

        if c.name in TAGS:
            wrap = getattr(markgen, TAGS[c.name])

            kwargs = {}
            if c.name in ATTRS:
                for attr, attr_map in ATTRS[c.name]:
                    if attr in c.attrs:
                        kwargs[attr_map] = c.attrs[attr]

            if c.name in LISTS:
                value = c.find_all('li')
            else:
                value = c.string

            c = wrap(value, **kwargs)

        out += u"\n{0}".format(c)

    return out
