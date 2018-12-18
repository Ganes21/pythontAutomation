"""
a group of code which can perform a specific task
methods are reusable and can be called when needed in the code
"""
def method_return(a,b,c):
   """

   :param a:
   :param b:
   :param c:
   :return:
   """
   return a+b+c

sum1=method_return(1,2,3)
str=method_return('uday','kanth','mallampalli')
print(sum1)
print(str)

def ifMetro(city):
    l=['sfa','la','nyc']
    if city in l:
        return True
    else:
        return False
x=ifMetro("nyc")
print(x)
y=ifMetro("hyd")
print(y)
