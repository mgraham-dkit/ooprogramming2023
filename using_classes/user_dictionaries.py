from User import User


def populate(filename):
    users = {}
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
                # Create a User object
                user = User()
                # Fill the User object with data
                user.username = user_data[0]
                user.password = user_data[1]
                user.fName = user_data[2]
                user.lName = user_data[3]
                # Store the data under the username (as the key) - the user's info will be stored as a list (i.e. the value is a list)
                users[user_data[0]] = user

    # Return the final dictionary of info
    return users

'''
    Function to get a valid username. 

    Valid is deemed to be not already present as a key in the supplied dictionary
'''
def get_valid_username(users):
    valid = False
    # While no valid username has been supplied
    while not valid:
        # Prompt for a username and store
        username = input("Please enter the new user's username: ")
        # If the username is not already a key in the dictionary
        if username not in users:
            # Deem the username as valid
            valid = True
        else:
            print("Username taken!")
    # Return the validated username
    return username

'''
    Function to save all users from a dictionary into a specified CSV file.

    Dictionary is assumed to have: 
        key as username (a string)
        value as user info made up of username, password, first name, last name (a list)
'''
def save(users, filename):
    # Open a link to the specified file name, in overwrite mode
    with open(filename, "w") as file_handle:
        # For each value in the dictionary, extract the username, password, first name and last name
        for user in users.values():
            # Output the user info to the file in a formatted manner
            file_handle.write(f"{user.username},{user.password},{user.fName},{user.lName}\n")


# Create a dictionary of user information from a specified csv file
users = populate("users.csv")
# Display it to confirm it worked
for user in users.values():
    user.display()

# Request a valid (i.e. unique, not already present in the dictionary) username from the user
username = get_valid_username(users)
# Take in remaining user information
password = input(f"Please enter the password for {username}: ")
fName = input(f"Please enter the first name for {username}: ")
lName = input(f"Please enter the last name for {username}: ")

# Create list of user information
user = User()
user.username = username
user.password = password
user.fName = fName
user.lName = lName
# Store new user in the contacts dictionary
users[username] = user
# Save the contacts dictionary to a csv file
save(users, "users.csv")