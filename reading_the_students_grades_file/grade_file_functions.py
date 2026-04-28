class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        return open(self.file_name)

class StudentFile:
    def __init__(self, file_handle):
        self.file_handle = file_handle

    def extract_data(self):
        data_pairs = []
        with self.file_handle:
            for line in self.file_handle:
                line = line.strip()
                if not line:
                    continue
                line = line.replace("=", " ")
                parts = line.split()
                if len(parts) >= 2:
                    data_pairs.append([parts[0], parts[1]])
        return data_pairs

    def get_names(self, data_pairs):
        return [pair[0] for pair in data_pairs]

    def get_grades(selfself, data_pairs):
        return [int(pair[1]) for pair in data_pairs]

class GradeAnalyzer:
    def __init__(self, student_names, student_grades):
        self.names = student_names
        self.grades = student_grades

    def find_top(self):
        max_grade = max(self.grades)
        index = self.grades.index(max_grade)
        top_student = self.names[index]
        return max_grade, index, top_student

