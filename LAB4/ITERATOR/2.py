class number:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        value=self.a
        self.a+=1
        return value
values=number()
n=int(input('even number '))
for i in range(n):
    if i % 2==0:
        print(i)