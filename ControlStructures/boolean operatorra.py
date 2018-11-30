''''
and
true and true --> true
True and false--> false
false and false-->false
or
true or true-->true
true or false-->false
false or false-->false

not
'''

o1=(10==10)and (10>9)
print(o1)
o2=(10==10) and (10<9)
print(o2)
o3=(10!=10) and (10<9)
print(o3)
print("**********")
o4=(10==10)or (10>9)
print(o4)
o5=(10==10) or (10<9)
print(o5)
o6=(10!=10) or (10<9)
print(o6)
print("**********")

o7=not(10==10)
print(o7)

o8=not(10!=10)
print(o8)


