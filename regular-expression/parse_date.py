import re


def parse_date(text):
    pattern = re.compile(r'^(?P<d>\d{2})(/|\.|,)(?P<m>\d{2})(/|\.|,)(?P<y>\d{4})$')
    match = pattern.match(text)
    if match:
        return {"d": match.group('d'), "m": match.group('m'), "y": match.group('y')}
    else:
        return None


print(parse_date('12/02/2342'))
print(parse_date('12,02,2342'))
print(parse_date('12.02.2342'))
print(parse_date('12/032/2342'))
