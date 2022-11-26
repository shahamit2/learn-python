class Sweet:
    class _sweet_iter:
        def __init__(self, sweets):
            self.sweets = sweets
            self.cur = 0

        def __next__(self):
            i = self.cur
            if i >= len(self.sweets):
                raise StopIteration
            self.cur += 1
            return self.sweets[i]

    def __init__(self):
        self.sweets = []

    def add(self, name):
        self.sweets.append(name)
        return self

    def __iter__(self):
        return Sweet._sweet_iter(self.sweets)

# Main
sweets = Sweet()
sweets.add("Coco")
sweets.add("Lassi")
for sweet in sweets:
    print(sweet)
    print(id(sweet))