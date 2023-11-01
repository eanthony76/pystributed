import pandas as pd
import os

# Ensure the directory exists
directory = "/home/results"
if not os.path.exists(directory):
    os.makedirs(directory)

# Write to the file within the directory
file_path = os.path.join(directory, "file.txt")

a = 8
b = 19
c = a+b

with open(file_path, 'w') as f:
    f.write(str(c))
    f.close()
