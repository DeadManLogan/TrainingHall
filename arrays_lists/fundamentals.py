# In-Memory Table
class Table:
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def delete_row(self, index):
        del self.rows[index]

    def find_rows(self, value):
        res = []
        for row in self.rows:
            if value in row:
                res.append(row)
        return res

t = Table()
t.add_row(["Alice", 30])
t.add_row(["Bob", 25])
t.add_row(["Carol", 30])

print(t.find_rows(30))
t.delete_row(1)
