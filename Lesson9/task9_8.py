import re


def get_url(text: str) -> list[str]:
    """Returns url list found in the input text"""
    pattern = (r'\b'
               r'(?:https?://|www\.)'
               r'(?=[a-z0-9.-]*[a-z])'
               r'[a-z0-9-]+'
               r'(?:\.[a-z0-9-]+)+'
               r'(?:/[^\s?#]*)?'
               r'(?:\?[^\s#]*)?'
               r'(?:#[^\s]*)?\b')
    return re.findall(pattern, text, flags=re.IGNORECASE)


text_notes = """
Check out the search engine at https://www.google.com (valid) and the tutorial at http://example.org/page (valid). 
Some sites might omit the scheme like www.testsite.com (valid), but beware of typos like htp://badurl.com (invalid). 
Also, malformed URLs like http://example..com (invalid) or just text like www.example..org (invalid) should be ignored. 
Secure sites like https://sub.domain.co.uk/path?query=123 (valid) are okay. 
Random text www.fake-site- (invalid) and http://256.256.256.256 (invalid) are not valid URLs.
"""
print(get_url(text_notes))

expected_result = ['https://www.google.com', 'http://example.org/page',
                   'www.testsite.com', 'https://sub.domain.co.uk/path?query=123']

def test_get_url():
    assert get_url(text_notes) == expected_result
