def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            lines = file.readlines()

        # Modify content and write to the new output file
        with open(output_filename, 'w') as file:
            for line in lines:
                file.write(line.strip() + " - Modified\n")

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")

# Ask user for the input and output filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write the modified content: ")

modify_file(input_filename, output_filename)
