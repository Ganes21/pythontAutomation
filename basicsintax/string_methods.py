#accessing char from string
n="nyc"
print(n)

print(n[2])

c="city"
s=c[2:]
print(s)

"""
len()
lower()
upper()
"""

s="oneabctwoabcthreeabc"
print(s.replace("abc","Abc",4))

t="mallampalliudaykanth"
sub=t
print(sub)
print(sub[1:9:2])
print(sub[1:9:1])
print(sub[1:9])
print(sub[9:-1])
print(sub[::2])
print(sub[::-1])
s=input("enter string")
"""if s==s[::-1]:
    print("string is \"pallendrom\"")
else:
    print("string is not pallendrom")
"""
v=input("enter input")
b=input("enter input two")
print("welcome to%s and enjoy%s"%(v,b))

l=sub.split()
print(l)
