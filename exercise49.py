from os import listdir
from os.path import isfile, join

directory = r'C:\Users\user\Desktop\GitHub\Python\python_basic_part1'
file_list = [f for f in listdir(directory) if isfile(join(directory, f))]
print(file_list)
