import re


def parse_bytes(text):
    pattern = re.compile(r'\b[01]{8}\b')
    return pattern.findall(text)


print(parse_bytes('11100001 11100'))
print(parse_bytes('My data is 1110000111100'))
print(parse_bytes('11100001 11100'))
