class OneIndexedList:

    def __init__(self, items=None):
        self.items = items or []

    def __getitem__(self, idx):
        return self.items[idx-1]

a = OneIndexedList([])
a.items.append(0)
print(a[1])