class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(selfself):
        """Reads numbers from the file and returns them as a list of integers"""
        numbers = []
        with open(self.file_name, r) as file:
            for line in file:
                if line.strip():
                    numbers.append(int(line.strip()))
        return numbers

class NumberProcessor:
    @staticmethod
    def seperate_even_odd(numbers):
        """Splits numbers into even and odd lists, then returns formatted strings"""
        evens = []
        odds = []
        for num in numbers:
            if num % 2 == 0:
                evens.append(str(num))
            else:
                odds.append(str(num))
        return ", ".join(evens), ", ".join(odds)

class FileWriter:
    @staticmethod
    def write_results(even_str, odd_str):
        """Writes the even and odd number strings to separate files."""
        with open("even_numbers.txt", "w") as even_file:
            even_file.write(even_str)
        with open("odd_numbers.txt", "w") as odd_file:
            odd_file.write(odd_str)
            