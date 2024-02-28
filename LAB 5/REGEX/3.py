import re
def ajratish(text):
    misol1=re.split(text)
    misol=misol1.upper()
    if ajratish(text,misol):
        return True
    else:
        return False
result=input('enter a string: ')
if ajratish(result):
    print('yes')
else:
    print('no')