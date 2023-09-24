secondary_contacts = {
    "helen" : "088 3917 283",
    "William" : "085 1736 128"
}

primary_contacts = {
    "Helena" : "086 3917 283",
    "William" : "085 1736 128"
}

final_contacts = {}
for k, v in secondary_contacts.items():
    final_contacts[k] = v

conflicts = {}
for k, v in primary_contacts.items():
    if k not in final_contacts:
        final_contacts[k] = v
    else:
        conflicts[k] = v

print("Final contact book:", final_contacts)
print("Conflicts from second contact book:", conflicts)