import re


def get_ipv4_address(text:str) -> list[str]:
    """Returns ip address list found in the input text"""
    num_pattern = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    ip_pattern = (rf"(?<![\d.])"
                 rf"(?:{num_pattern}\.){{3}}{num_pattern}"
                 rf"(?![\d]|\.[\w])")
    return re.findall(ip_pattern, text)


text_notes = """
The network configuration is complete. The primary server is hosted at 192.168.1.1, 
while the backup database can be reached at 10.0.0.254. 
We also have a local testing environment on 127.0.0.1.
During the setup, some engineers entered incorrect values that should be ignored by the script:
999.1.1.1 (Invalid: first octet is out of range)
172.16.256.1 (Invalid: third octet is above 255)
192.168.1.1.1 (Invalid: has five octets, your script should ignore the whole thing)
1.2.3 (Invalid: too short)
https://www.google.com/search?q=8.8.8.8.com (Invalid: part of a domain name)
210.110.55.999 (Invalid: last octet is too high)
Please ensure that addresses like 172.16.0.1 are captured, 
but strings like 333.444.555.666 are completely filtered out.
"""

expected_ip_list = ['192.168.1.1', '10.0.0.254', '127.0.0.1', '172.16.0.1']


def test_get_ipv4_address():
    assert get_ipv4_address(text_notes) == expected_ip_list
