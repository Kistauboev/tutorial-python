def myfunction():
    global x, y
    x = 5
    y = 4
    print(x, y)
    if x > y:
        print("YES")
    else:
        print("NO")

myfunction()
