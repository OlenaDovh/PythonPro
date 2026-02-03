import re


def delete_html_tags(html: str) -> str:
    """Deletes html tags in teh input text and makes it into the readable formate"""
    no_tags_lines = []
    for line in html.splitlines():
        line_with_no_tags = re.sub(r"<[^>]+>", " ", line).lstrip().rstrip()
        if line_with_no_tags:
            no_tags_lines.append(line_with_no_tags)
    return "\n".join(no_tags_lines)


html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>
    Sample Page
    </title>
</head>
<body>
<h1>Welcome to <span>My Website</span></h1>
<p>
    This is a <strong>sample</strong> paragraph with
    <a href="https://example.com">a link</a>
    and some <em>emphasized text</em>.
</p>
<div class="content">
    <p>Another paragraph inside a div.</p>
    <ul>
        <li>First item</li>
        <li>Second <b>bold</b> item</li>
        <li>Third item</li>
    </ul>
</div>
<img src="image.jpg" alt="Sample image">
<br>
<footer>
    <p>Contact us at <a href="mailto:test@example.com">test@example.com</a></p>
</footer>
</body>
</html>
"""

expct_rslt = """Sample Page
Welcome to  My Website
This is a  sample  paragraph with
a link
and some  emphasized text .
Another paragraph inside a div.
First item
Second  bold  item
Third item
Contact us at  test@example.com"""


def test_delete_html_tags():
    assert delete_html_tags(html_page) == expct_rslt
