"""
positional parameters are like optional paremeters and
cam be assigned a default value ,if no value is provided outside
"""
def sum_num(n1=6,n2=9):
    '''

    :param n1:
    :param n2:
    :return:
    '''
    return n1+n2
sum1=sum_num(11,2)
print(sum1)
print("*****************")
sum2=sum_num(2,8)
print(sum2)
print("*****************")
sum3=sum_num(n1=2,n2=16)
print(sum3)
print("*****************")
sum4=sum_num(n2=6,n1=9)
print(sum4)
print("*****************")
sum5=sum_num(n2=5)
print(sum5)
sum6=sum_num(n1=6)
print(sum6)


def su_nu(n1,n2=9):
    return n1+n2
sumone=su_nu(2,9)
print(sumone)
print("*****************")
sumtwo=su_nu(9)
print(sumtwo)
