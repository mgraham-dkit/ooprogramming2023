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
            invalid_file = False
            line_count = 0

            # Read content of file in and store in a list of content
            for line in file_handle:
                line_count += 1
                line = line.strip()
                components = line.split("%%")
                data = []

                try:
                    data.append(components[1])
                except IndexError as e:
                    print(f"No element found at position 1 (ID information) on line {line_count}: \"{line}\"")
                    print(f"Arguments: {e.args}")
                    continue
                    
                try:
                    data.append(components[2])
                except IndexError as e:
                    print(f"No element found at position 2 (Name information) on line {line_count}: \"{line}\"")
                    print(f"Arguments: {e.args}")
                    continue

                try:
                    data.append(float(components[3]))
                except IndexError as e:
                    print(f"No element found at position 3 (Cost price information) on line {line_count}: \"{line}\"")
                    print(f"Arguments: {e.args}")
                    continue

                try:
                    data.append(float(components[4]))
                except IndexError as e:
                    print(f"No element found at position 4 (Retail price information) on line {line_count}: \"{line}\"")
                    print(f"Arguments: {e.args}")
                    continue

                try:
                    data.append(int(components[5]))
                except IndexError as e:
                    print(f"No element found at position 5 (Quantity information) on line {line_count}: \"{line}\"")
                    print(f"Arguments: {e.args}")
                    continue

                if components[0] == "Book":
                    try:
                        data.append(components[6])
                    except IndexError as e:
                        print(
                            f"No element found at position 6 (Author information) on line {line_count}: \"{line}\"")
                        print(f"Arguments: {e.args}")
                        continue

                    try:
                        genres = components[7].split("&&")
                        data.append(genres)
                    except IndexError as e:
                        print(
                            f"No element found at position 6 (Author information) on line {line_count}: \"{line}\"")
                        print(f"Arguments: {e.args}")
                        continue

                # Display data for this line
                display(data)

    except FileNotFoundError as e:
        print("Invalid filename provided. Please enter a new file name")
        print(f"Exception details: {e.args}")
