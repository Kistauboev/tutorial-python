import re
txt='the rain in spain'
x=re.findall('ai', txt)
if x:
    print('yes includes in the word spain and rain')
else:
    print('no this word ')  

import re
txt='the rain in spain'
x=re.findall('in', txt)
print(x)

 # findall() - we use when we want some in string 'in' if we write without if it outputs just occurence of 'in' such as [ 'in' 'in' ] and so on