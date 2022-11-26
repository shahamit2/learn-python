# Build class with iterator methods.
class PowTwo:
    def __init__(self, startnum, endnum):
        self.startnum = startnum
        self.endnum = endnum
    def __iter__(self):
        return self
    def __next__(self):
        if self.startnum <= self.endnum:
            result = 2 ** self.startnum
            self.startnum += 1
            return result
        else:
            raise StopIteration


# __iter__ and __next__ together called as iterator protocol.
# Way 1
for i in PowTwo(1,5):
    print(i)
    print(id(i))

# Way 2
a = PowTwo(1,5)
next(a)
next(a)
