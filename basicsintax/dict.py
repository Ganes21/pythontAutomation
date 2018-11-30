cars={"make":"bmw","model":89,"year":2016}
print(cars)

print(list(enumerate(cars)))

print(cars["model"])

d={}
print(d)
d["one"]=1
print(d)
d["two"]= 2
print(d)

s=d["one"]+9
print(s)
d['one']=d["two"]+9
print(d)
''''
nested doctrinaires
'''
nd={"k1":{"value1":"one","value2":"two"}}
car={"bmw":{"model":"500i","year":2017},"benz":{"model":"500i","year":2017}}
print(car)
print(car["bmw"]["model"])
print(list(enumerate(car)))

