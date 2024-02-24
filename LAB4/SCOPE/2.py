x=300
def outer():
    print(x)
    def inner():
        print(x)
    inner()
outer()
