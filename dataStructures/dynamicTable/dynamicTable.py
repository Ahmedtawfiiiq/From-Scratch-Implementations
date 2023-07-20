class DynamicTable:
    def __init__(self):
        self.table = [None]
        self.size = 0
        self.capacity = 1

    def resize(self):
        self.capacity *= 2
        newTable = [None] * self.capacity
        for i in range(self.size):
            newTable[i] = self.table[i]
        self.table = newTable

    def add(self, item):
        # add item to the end of the table
        if self.size == self.capacity:
            self.resize()
        self.table[self.size] = item
        self.size += 1

    def delete(self):
        # delete the last item
        self.table[self.size - 1] = None
        self.size -= 1

    def insert(self, item, index):
        # insert item at a given index
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.table[i] = self.table[i - 1]
        self.table[index] = item
        self.size += 1

    def remove(self, index):
        # delete the item at a given index
        for i in range(index, self.size - 1):
            self.table[i] = self.table[i + 1]
        self.table[self.size - 1] = None
        self.size -= 1


t = DynamicTable()
for i in range(10):
    t.add(i)
print(t.table)
t.insert(14, 5)
print(t.table)
t.remove(6)
print(t.table)
t.delete()
print(t.table)
