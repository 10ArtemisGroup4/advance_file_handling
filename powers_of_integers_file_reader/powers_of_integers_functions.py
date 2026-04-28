class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        """Open and return the file handle."""
        return open(self.file_name)

    