from bs4 import BeautifulSoup


def markup_to_markdown(content):
    soup = BeautifulSoup(content)

    # Account for HTML snippets and full documents alike
    contents = soup.body.contents if soup.body is not None else soup.contents

    for c in contents:
        pass
