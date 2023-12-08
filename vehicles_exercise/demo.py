from transport import Vehicle

vehicle = Vehicle("Rover", "red", 5)
vehicle2 = Vehicle("Honda", "blue", 5)
print("Vehicle : ", str(vehicle))

print(vehicle == vehicle2)
print(vehicle != vehicle2)

fleet = [vehicle, vehicle2]
fleet.sort()
print(fleet)