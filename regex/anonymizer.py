import re

pattern = re.compile(r"""
    (?P<email> [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}) |
    (?P<phone> \+?\d[\d\s\-()]{7,}\d) |
    (?P<ip>    \b\d{1,3}(?:\.\d{1,3}){3}\b)
""", re.X)

def anonymize(text):
    def replace(match):
        if match.group("email"):
            return "[EMAIL]"
        elif match.group("phone"):
            return "[PHONE]"
        elif match.group("ip"):
            return "[IP]"
    return pattern.sub(replace, text)

text = """
User jack.sparrow@pirate.cb logged in from 192.168.0.10
Backup contact: +1 (555) 123-4567 or jane@mail.co.uk
"""

print(anonymize(text))


