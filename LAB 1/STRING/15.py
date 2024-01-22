"""
age=36
txt='my name is john ' + age
print(txt)  #biz string va sonni + orqali yoz olmaymiz
"""

#format() - dan foydalanmiz qaconki string va int qatnashgan sonni biriktishda va albatta {} orqali foydalanmiz
age=36
txt='my name is jon, and I am {}'
print(txt.format(age))
