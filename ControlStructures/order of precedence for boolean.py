'''
not and or
'''
o1=True or not False and False
print(o1)
""""
True  and false--> false
true or false -->true
"""

o2=10==10 or not 10>10 and 10>10
"""
not10>10-->false
false and false --> true
true or false-->true
"""
print(o2)

o3=(10==10 or not 10>10) and 10>10
"""
false or true-->true
true and false --> false
"""
print(o3)


k="kishore"
print(k[::-1])
print(list(enumerate(k)))
