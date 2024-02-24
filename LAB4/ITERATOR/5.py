class numbers:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        value=self.a
        if value<=20:
            self.a+=1
            return value
        else:
            raise StopIteration
values=numbers()
it=iter(values)
for i in it:
    print(i)
