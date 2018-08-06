import re


def is_valid_time(t):
    pattern = re.compile(r"^\d{1,2}:\d{2}$")
    return True if pattern.match(t) else False


print(is_valid_time("12:34"))
print(is_valid_time("1234"))
print(is_valid_time("2:34"))
print(is_valid_time("72:34"))
print(is_valid_time("72:4"))
