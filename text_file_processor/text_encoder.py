from text_file_encoding_functions import FileHandling, InputText

file_name = "my_notes.txt"

file_handler = FileHandling(file_name)
file_handle = file_handler.open_file()

print("Start typing your notes. Type 'n' when done.\n")

while True:
    line = InputText.get_input()
    file_handler.append_input(file_handle, line)

    more = InputText.get_second_input()
    if more.lower() != 'y':
        break

file_handle.close()
print(f"\nAll lines saved to {file_name}")