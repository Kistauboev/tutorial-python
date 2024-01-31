 # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
 # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x=('banana', 'kiwi', 'ananas', 'pear', 'apple', 'peach', 'cherry')
y=list(x)
y[3]='kiwi'
x=tuple(y)
print(x)