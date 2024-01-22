#biz funksiyani icida yaratsak bu inside function buladi biz uni icida turgan holini global qilmoqci bulsak inside function ga global deb kiritamiz
def myFunc():
    global x
    x='fantastic'
myFunc()
print(f"Python is {x}")

