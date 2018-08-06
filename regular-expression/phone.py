import re


def extract_phone(text):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(text)
    if match:
        return match.group()
    else:
        return None


def is_valid_phone(text):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.match(text)
    return True if match else False


print(extract_phone("123 345-4567 this is my number"))
print(extract_phone("123 345-456756 this is my number"))
print(is_valid_phone("123 456-7896"))
print(is_valid_phone("123 456-7896 This is my number"))
