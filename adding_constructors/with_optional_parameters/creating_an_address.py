from Address import Address


# You can create a new Address object in one of a couple of ways:
# Create it with JUST required fields - this will fill in all of the core values
# but leave out line2 and line 3
address_required_only = Address("Uluru", "Great Maltings", "Donabate", "Dublin", "A61 SW32", "Ireland")
address_required_only.display()

# Create it with all of the required fields and ONE of the optional fields
# (you can specify which one by naming it)
address_with_line3 = Address("Uluru", "Great Maltings", "Donabate", "Dublin", "A61 SW32", "Ireland", line3="Line 3!")
address_with_line3.display()

# Create it with all of the required fields and BOTH of the optional fields
complete_address = Address("Uluru", "Great Maltings", "Donabate", "Dublin", "A61 SW32", "Ireland", "Line 2", "Line 3!")
complete_address.display()
complete_address.