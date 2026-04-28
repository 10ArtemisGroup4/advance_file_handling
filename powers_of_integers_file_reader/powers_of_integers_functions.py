class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        """Open and return the file handle."""
        return open(self.file_name)

class IntegerFunctions:
    def __init__(self, file_handle):
        self.file_handle = file_handle

    def get_integers(self):
        """Read all integers from the file and return them as a list of ints."""
        numbers = []
        with self.file_handle:
            for line in self.file_handle:
                line = line.strip()
                if line:
                    numbers.append(int(line))
        return numbers

    def square_integers(self, numbers):
        """Return a comma-separated string of squared numbers."""
        squares = [str(n ** 2) for n in numbers]
        return", ".join(squares)

    def cube_integers(self, numbers):
        """Return a comma-separated string of cubed numbers."""
        cubes = [str(n ** 3) for n in numbers]
        return", ".join(cubes)

class WriteFile
    def __init__(self, squared_data, cubed_data):
        self.squared_data = squared_data
        self.cubed_data = cubed_data

    def write_files(self):
        """Write squared numbers to double.txt and cubed numbers to triple.txt."""
        with open("double.txt", "w") as sq_file:
            sq_file.write(self.squared_data)
        with open("triple.txt", "w") as cu_file:
            cu_file.write(self.cubed_data)
            