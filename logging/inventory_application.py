import logging
from products import Product
from products import Book


def load(file):
    position_info = ["Type", "ID", "name", "cost price", "retail price", "quantity", "author", "genres"]
    with open(file, "r") as file_handle:
        line_count = 0
        inventory = {}

        # Read content of file in and store in a list of content
        for line in file_handle:
            line = line.strip()
            line_count += 1
            component_count = 1
            components = line.split("%%")

            try:
                id = components[component_count]
                component_count += 1
                name = components[component_count]
                component_count += 1
                cost_price = float(components[component_count])
                component_count += 1
                retail_price = float(components[component_count])
                component_count += 1
                quantity = int(components[component_count])
                component_count += 1

                if components[0] == "Book":
                    author = components[component_count]
                    component_count += 1
                    genres = components[component_count].split("&&")

                    item = Book(id, name, cost_price, retail_price, quantity, author, genres)
                else:
                    item = Product(id, name, cost_price, retail_price, quantity)
                if id in inventory:
                    raise KeyError("ID already exists")
                inventory[id] = item
            except IndexError as e:
                # Add logger warning call
                print(f"No element found for {position_info[component_count]} on line {line_count}: \"{line}\"")
                continue
            except KeyError as e:
                # Add logger warning call
                print(f"Id {id} already in use : \"{line}\"")
                continue

    return inventory


# Add logger configuration/set up
# Create a file handler and link it to a specific file
log_file = logging.FileHandler(filename="log_file.txt", mode="a")
# Set the level at which the handler is going to listen
log_file.setLevel(logging.WARNING)
# Set up the logger's details:
    # Handler to use
    # Level at which it will listen
    # Format of each log message
logging.basicConfig(level=logging.INFO, handlers=[log_file],
                    format='%(asctime)s :: %(levelname)s : %(message)s')

# Get dedicated logger for this program
logger = logging.getLogger("main")

invalid_file = True
while invalid_file:
    try:
        # Ask user to enter a filename
        filename = input("Please enter the inventory filename: ")
        print(f"Loading {filename}:")
        inventory = load(filename)
        invalid_file = False
    except FileNotFoundError as e:
        print("Invalid filename provided. Please enter a new file name")
        # Add logger warning call
        logger.error(f"{e.__class__.__name__} Error {filename} file not found")

print("Data intake complete.\n")
print("Inventory listing:")
for value in inventory.values():
    value.display()
