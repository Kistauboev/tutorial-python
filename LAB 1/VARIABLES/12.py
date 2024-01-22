x=1
def inner():
    x=3
    print(f'inner sees x equal to {x}')   #def inner faqat ichki funksiyani ciqaradi va uni yakunlab quyamiz yani inner() orqali
    return 
inner()
def outer():
    x=2
    print(f'outer sees x equal to {x}')  #bu ham inner lekin ajralib turishi ucun outer deb nomladik va bu 2 ni ciqaradi cunki def outer() ning icida
outer()
print(f'global sees x equal to {x}')  #bu esa global bu birincimkiritgan 1 ni ciqaradi.
 
