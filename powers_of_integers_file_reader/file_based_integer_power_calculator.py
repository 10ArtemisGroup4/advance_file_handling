from powers_of_integers_functions import OpenFile, IntegerFunctions, WriteFile

file_name = "integers.txt"

try:
    file_opener = OpenFile(file_name)
    file_handle = file_opener.open_file()

    processor = IntegerFunctions(file_handle)
    numbers = processor.get_integers()

    squares_str = processor.square_integers(numbers)
    cubes_str = processor.cube_integers(numbers)

    writer = WriteFile(squares_str, cubes_str)
    writer.write_files()

    print("Success! Results written to double.txt and triple.txt")

except FileNotFoundError:
    print(f"Error: The file {file_name} could not be found.")
except Exception as e:
    print(f"Error: {e}")