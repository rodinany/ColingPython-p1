class ReverseIter:
    def __init__(self, items=None):
        self.items = items or []
        self.n = len(items)

    def __getitem__(self, idx):
         return self.items[idx-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            n = self.n
            self.n -= 1
            return self[n]
        else:
            raise StopIteration()