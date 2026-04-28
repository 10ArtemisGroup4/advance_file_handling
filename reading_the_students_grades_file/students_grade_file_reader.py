from grade_file_functions import OpenFile, StudentFile, GradeAnalyzer

file_name = "grades.txt"

try:
    opener = OpenFile(file_name)
    file_handle = opener.open_file()

    processor = StudentFile(file_handle)
    data_pairs = processor.extract_data()
    names = processor.get_names(data_pairs)
    grades = processor.get_grades(data_pairs)

    analyzer = GradeAnalyzer(names, grades)
    max_grade, idx, top_name = analyzer.find_top()

    print("Top Student: " + top_name)
    print(f"Grade: {max_grade}")

except FileNotFoundError:
    print("Error: The file 'grades.txt' was not found.")
except Exception as e:
    print("An error occurred: ", e)