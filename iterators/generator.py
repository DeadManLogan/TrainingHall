def log_reader(path):
    with open(f"iterators/{path}") as file:
        for line in file:
            if "ERROR" in line or "WARN" in line:
                yield line.rstrip()

for line in log_reader("samples.txt"):
    print(line)
