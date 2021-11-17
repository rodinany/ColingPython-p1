class MinStack(object):

    def __init__(self, items=None):
        self.items = items or []
        self.min_items = []

    def push(self, val):
        if self.items:
            if val <= self.min_items[-1]:
                self.min_items.append(val)
        else:
            self.min_items.append(val)
        self.items.append(val)

    def pop(self):
        if self.items[-1] == self.min_items[-1]:
            self.min_items.pop()
        self.items.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.min_items[-1]
