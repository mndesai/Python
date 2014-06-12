cars=100 #number of cars
space_in_a_car=4 #spots in the car
drivers=30 #how many drivers there are
passengers=90 #number of passengers
cars_not_driven=cars - drivers #cars can't be driven without drivers
cars_driven=drivers #define cars driven as equal to number of drivers
carpool_capacity=cars_driven*space_in_a_car #total number of spots in the car for passengers
average_passengers_per_car=passengers/cars_driven #divide passengers by cars driven to get passengers per car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"