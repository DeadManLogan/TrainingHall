class LogReader:
    def __init__(self, path):
        self.file = open(f"iterators/{path}")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            return line.rstrip()
