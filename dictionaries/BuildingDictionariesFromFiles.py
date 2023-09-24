'''
    Function to read in from a file with a specified filename.

    This function assumes that the file is formatted as a CSV (comma separated values) file
'''
def populate(filename):
    contacts = {}
    # Open a link to the specified file in read-only mode
    with open(filename, "r") as file_handle:
        # For each line in the file
        for line in file_handle:
            # Strip off any excess padding at start and end
            line = line.strip()
            # Break up the content of the line into pieces (based on ,)
            user_data = line.split(",")
            # If the line is correctly formatted, i.e. has 4 components
            if len(user_data) == 4:
                # Store the data under the username (as the key) - the user's info will be stored as a list (i.e. the value is a list)
                contacts[user_data[0]] = user_data

    # Return the final dictionary of info
    return contacts

'''
    Function to get a valid username. 
    
    Valid is deemed to be not already present as a key in the supplied dictionary
'''
def get_valid_username(contacts):
    valid = False
    # While no valid username has been supplied
    while not valid:
        # Prompt for a username and store
        username = input("Please enter the new user's username: ")
        # If the username is not already a key in the dictionary
        if username not in contacts:
            # Deem the username as valid
            valid = True
    # Return the validated username
    return username

'''
    Function to save all contacts from a dictionary into a specified CSV file.
    
    Dictionary is assumed to have: 
        key as username (a string)
        value as user info made up of username, password, first name, last name (a list)
'''
def save(contacts, filename):
    # Open a link to the specified file name, in overwrite mode
    with open(filename, "w") as file_handle:
        # For each value in the dictionary, extract the username, password, first name and last name
        for user, passWd, first, last in contacts.values():
            # Output the user info to the file in a formatted manner
            file_handle.write(f"{user},{passWd},{first},{last}\n")


# Create a dictionary of contact information from a specified csv file
contacts = populate("contacts.csv")
# Display it to confirm it worked
print(contacts)

# Request a valid (i.e. unique, not already present in the dictionary) username from the user
username = get_valid_username(contacts)
# Take in remaining user information
password = input(f"Please enter the password for {username}: ")
fName = input(f"Please enter the first name for {username}: ")
lName = input(f"Please enter the last name for {username}: ")

# Create list of user information
user = [username, password, fName, lName]
# Store new user in the contacts dictionary
contacts[username] = user
# Save the contacts dictionary to a csv file
save(contacts, "contacts.csv")