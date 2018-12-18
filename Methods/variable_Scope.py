"""
variable scope
"""

a=10
def test_method(a):
    print("Value of local a is",a)
    a=2
    print("Value of local a is ",a)
print("The  value of global a is",a)
test_method(15)
print("The value of global a is ",a)
print("**********************************")

b=10
def test_methodone():
    global b
    print("Value of inside the method b is",b)
    b=2
    print("Value of inside the method after b is ",b)
print("The  value of global b is",b)
test_methodone()
print("The value of global b is ",b)

