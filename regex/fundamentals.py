import re

# log = """
# [2025-11-02 08:32] System Error: 504 - Timeout
# [2025-11-02 08:33] User Error: 404 - Not Found
# [2025-11-02 08:34] Debug Info: All clear
# [2025-11-02 08:35] System Error: 500 - Internal
# """
# # Write a regex using re.findall() to capture all error codes.
# pattern = r"Error:\s*(\d{3})" # parenthesis return only what's inside. \s* makes sure to match what comes after Error:
# res = re.findall(pattern, log)
# print(res)



files = "sales.csv notes.txt report.csv data.log archive.csv"
# Your goal: ['sales.csv', 'report.csv', 'archive.csv']
pattern = r"\w+\.csv"
print(re.findall(pattern, files))
