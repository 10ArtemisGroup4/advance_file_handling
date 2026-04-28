class FileHandling:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        return open(self.file_name, 'a')

    def append_input(self, text_file, text_input):
        text_file.write("\n" + text_input)
        