import re

# # DUPLICATED WORDS
# text = "hello hello world world test"
# # 🎯 Expected result: ['hello', 'world']
# '''
# (\b\w+) → captures a full word (letters, digits, or underscore) with a word boundary before it.

# \s+ → allows any whitespace (space, tab, etc.) between words.

# \1 → reuses the exact word captured by the first group.
# '''
# pattern = r"(\b\w+)\s+\1"
# result = re.findall(pattern, text)
# print(result)


# # FLAGS
# log = """
# ERROR: 404 - Not Found
# info: ready
# error: 500 - Timeout
# Debug: done
# """

# # 🎯 Expected result: ['404', '500']
# pattern = re.compile(r"error:\s*(\d+)", re.I)
# for row in pattern.finditer(log):
#     print(row.group(1))


# # ASSERTIONS
# text = "USD100 EUR200 USD300 JPY400"
# # 🎯 Expected result: ['100', '300']
# pattern = r"(?<=USD)\d+"
# result = re.findall(pattern, text)
# print(result)


# # CONDITIONAL
# '''
# (?: ... ) → non-capturing group, to combine the two branches cleanly.

# VIP-\d{6} → matches VIP IDs with exactly 6 digits.

# (?!VIP-)\b\w{3}-\d{4}\b → matches non-VIP IDs:

# (?!VIP-) → negative lookahead ensures it’s not VIP.

# \w{3}-\d{4} → matches 3-letter prefix + 4-digit number.

# \b → word boundaries to avoid partial matches.
# '''
# ids = "VIP-123456 REG-1234 REG-12345 VIP-1234"
# pattern = r"(?:VIP-\d{6}|(?!VIP-)\b\w{3}-\d{4}\b)"
# result = re.findall(pattern, ids)
# print(result)




pattern = r"""
^                 # start of string
(?=.*[A-Z])       # at least one uppercase
(?=.*\d)          # at least one digit
(?=.*[!@#$%^&*])  # at least one special char
[A-Za-z\d!@#$%^&*]{8,}  # min length 8
$                 # end of string
"""

passwords = ["Pass123!", "weakpass", "Strong#1", "NoSpecial1"]

compiled = re.compile(pattern, re.X)
valid_passwords = [p for p in passwords if compiled.match(p)]
print(valid_passwords)
# Output: ['Pass123!', 'Strong#1']


