def outer():
    x=300
    print(x)
    def inner():
        print(x)
outer()