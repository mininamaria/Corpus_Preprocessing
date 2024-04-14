import os
from pymystem3 import Mystem

# Folder Path
path = "C:/Users/Maria/Desktop/temporary"

# Change the directory
os.chdir(path)
m = Mystem()

# Create text File


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        lemmas = m.lemmatize(f.read())
        with open('edited.txt', 'w') as f_to_w:
            f_to_w.write(''.join(lemmas))
        print("Mission complete! New file is ready!", file_path)


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"

        # call read text file function
        read_text_file(file_path)
