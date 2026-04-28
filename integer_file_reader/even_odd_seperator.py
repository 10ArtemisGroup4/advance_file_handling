from integer_functions import FileReader
from integer_functions import NumberProcessor
from integer_functions import FileWriter

file_name = "numbers.txt"

try:
    reader = FileReader(file_name)
    number_list = reader.read_numbers()

    even_numbers_str, odd_numbers_str = NumberProcessor.seperate_even_odd(number_list)

    FileWriter.write_results(even_numbers_str, odd_numbers_str)

except Exception as e:
    print("Error in Handling the Request.", e)