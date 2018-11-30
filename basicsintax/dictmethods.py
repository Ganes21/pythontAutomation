car={"bmw":{"model":"500i","year":2017},"benz":{"model":"500i","year":2017}}
cars={"make":"bmw","model":89,"year":2016}
print(cars.keys())
print(car.keys())
print(car.values())
print(cars.values())
print(car.items())
print(cars.items())

car_cpy=car.copy()
print(car_cpy)
print(cars.pop("model"))
print(cars)
