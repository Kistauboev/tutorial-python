def myfunc():
  global x
  x = 300
myfunc()

print(x)
 
# in this case x is the inside of the function. It will output error bcz 300 local, print()- is standing outside the function
# for this we used global to make 300 global
