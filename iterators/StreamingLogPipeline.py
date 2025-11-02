from LogReader import LogReader
from itertools import chain
# Each line looks like: "2025-11-01 10:42:00 ERROR Database timeout"

# Replaces the LogReader
def log_reader(path):
    with open(path) as file:
        for line in file:
            yield line.strip()

def multi_log_reader(paths):
    return chain.from_iterable(log_reader(p) for p in paths)

def filter_logs(lines):
    for line in lines:
        if "ERROR" in line or "WARN" in line:
            yield line

def parse_logs(lines):
    for line in lines:
        parts = line.split(" ", 3)
        timestamp = f"{parts[0]} {parts[1]}"
        level = parts[2]
        message = parts[3]
        yield f"[{timestamp}] {level} {message}"

# --- Pipeline assembly ---
paths = ["iterators/samples.txt", "iterators/samples2.log"]

lines = multi_log_reader(paths)
filtered = filter_logs(lines)
parsed = parse_logs(filtered)

for _ in parsed:
    print(_)
