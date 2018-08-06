import re


def censor(text):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    text = pattern.sub('CENSORED', text)
    return text


print(censor('frack'))
print(censor('I hope you fracking die.'))
print(censor('fracking'))
