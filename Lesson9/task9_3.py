import re


def get_hashtag(text: str) -> list[str]:
    """Returns hashtags from the input text"""
    return re.findall(r"#([A-Za-zА-Яа-яІіЇїЄє0-9]+)(?![_\w\-])", text)


text_notes = """
Today I started learning #python (valid) and quickly moved on to #Python3 (valid).
I’m especially interested in #python_dev (invalid) and #data_123 (invalid) projects.

Some people like to write #hello_World (invalid) or even #helloWorld (valid) in their posts.
Others experiment with AI and use #AI (valid) or topics like #машиннеНавчання. (valid).

However, not all hashtags are written correctly.
For example, # (invalid) is not a real hashtag.
The hashtag #hello-world (invalid) is also incorrect due to the hyphen.

Sometimes people start a hashtag with a special symbols such as # python (invalid) or #@data@science (invalid).
"""

expected_result = ['python', 'Python3', 'helloWorld', 'AI', 'машиннеНавчання']


def test_get_hashtag():
    assert get_hashtag(text_notes) == expected_result
