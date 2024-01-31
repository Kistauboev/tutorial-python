# intersection_update() - bu faqat ikkita set da mavjud bulgan qiymatni ciqaradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# symmetric_difference_update() - bu esa aksi ya'ni ikkalasi yuq bulgan qiymatlarni ciqaradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# isdisjoint() - bu agar ikkala set da ham har xil qiymat bulsa true deb ciqaradi ya'ni  x da boshqa y da boshqa bulsa 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)