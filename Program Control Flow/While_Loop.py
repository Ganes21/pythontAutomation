"""
loops Execute the statements repeately
"""
x=int(input("enter the number"))
while x<=10:
    print("Value of x is:"+str (x))
    x=x+2
l=[]
num=0
while num<10:
    l.append(num)
    print("The value of num: before" + str(num))
    num+=1
    print("The value of num:"+str(num))
print(l)

Count=0
while Count <=4:
    print("currently count is%d is before" % Count)
    Count +=1
    print("currently count is %d after"% Count)

c=10
while c<=30:
    print("the value of %d" %c)
    c += 1
n=10
sum=0
i= 1
while i<n:
    #sum=sum+i
    #print("befor iteration sum is",sum)
    i=i+1
    print("the value of i is aftere iteration %d"%i)
    #print("the value of sum after iteration %d"%sum)

#print("the sum is ",sum)
