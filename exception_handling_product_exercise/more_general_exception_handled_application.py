def display(data):
    print("Product details:")
    print(f"\tID: {data[0]}")
    print(f"\tName: {data[1]}")
    if len(data) == 7:
        print(f"\tAuthor: {data[5]}")
    print(f"\tCost price: {data[2]}")
    print(f"\tRetail price: {data[3]}")
    print(f"\tQuantity in stock: {data[4]}")
    if len(data) == 7:
        print(f"\tGenre(s): {data[6]}")


invalid_file = True
while invalid_file:
    try:
        # Ask user to enter a filename
        filename = input("Please enter the inventory filename: ")
        with open(filename, "r") as file_handle:
            line_count = 0

            # Read content of file in and store in a list of content
            for line in file_handle:
                line_count += 1
                line = line.strip()
                components = line.split("%%")
                data = []
                data.append(components[1])
                data.append(components[2])
                data.append(float(components[3]))
                data.append(float(components[4]))
                data.append(int(components[5]))

                if components[0] == "Book":
                    data.append(components[6])
                    genres = components[7].split("&&")
                    data.append(genres)

                # Display data for this line
                display(data)
        invalid_file = False
    except FileNotFoundError as e:
        print("Invalid filename provided. Please enter a new file name")
        print(f"Exception details: {e.args}")
    except IndexError as e:
        print(f"Missing element on line {line_count}: \"{line}\"")
        print(f"Arguments: {e.args}")
