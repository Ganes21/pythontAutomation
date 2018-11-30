a=153
b=60
c=50
d=40

if (a>b)and (a>c) and (a>d):
    pass
elif(b>a) and (b>c) and (b>d):
    print("b is greater")
elif(c>d)and(c>b)and (c>a):
    print("c is greater")
else:
    print("d is greater")
l=input("enter the car name ")
my_cars=["ford","bmw","audi","benz"]

if l in my_cars:
    print("ford is in list")
else:
    my_cars.append(l)
print (my_cars)

s="udaykanthmallampalli"
if "i" in s :
    print("The i is in ",s)

x ="test"
if len(x)== 5:
    print("the lenght is 5 ")

else:
    print(len(x))










