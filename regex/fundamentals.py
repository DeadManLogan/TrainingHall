import re

# DUPLICATED WORDS
text = "hello hello world world test"
# 🎯 Expected result: ['hello', 'world']
'''
(\b\w+) → captures a full word (letters, digits, or underscore) with a word boundary before it.

\s+ → allows any whitespace (space, tab, etc.) between words.

\1 → reuses the exact word captured by the first group.
'''
pattern = r"(\b\w+)\s+\1"
result = re.findall(pattern, text)
print(result)


