from House import House


my_home = House()
my_second_home = House()
print(f"Colour: {my_home.colour}")

my_home.colour = "Blue"
print(f"First home colour: {my_home.colour}")
print(f"Second home colour: {my_second_home.colour}")