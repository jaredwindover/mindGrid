class IntKey:
    def __init__(self, base = 0):
        self.base = base

    def get(self,n):
        if n == 0:
            return self.base
        else:
            return self.increment(self.get(n - 1))

    def increment(self,n):
        return n + 1
