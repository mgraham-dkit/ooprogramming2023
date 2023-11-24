from Staff import Staff


staff_member = Staff("Michelle", 22, "120 Hellfire Way", "11/12/2022", "Computing")
staff_member2 = Staff("Michelle", 22, "120 Hellfire Way", "11/12/2022", "Computing")
print(staff_member)
print(f"The wage for the staff member is {staff_member.calc_wage()}")

print("staff1 == staff2: ", staff_member == staff_member2)
print(hash(staff_member))
print(hash(staff_member2))