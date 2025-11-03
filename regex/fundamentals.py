import re

log = "Users: A123, b456, C789, D12E, E000"
# Desired result: ['A123', 'C789', 'E000']
pattern = r"[A-Z]\d{3}"
print(re.findall(pattern, log))

