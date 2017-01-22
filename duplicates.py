import os
import itertools
import filecmp
import sys

def are_files_duplicates(file_path1,file_path2):
    difference_files = filecmp.cmp(file_path1,file_path2)
    return  difference_files    

def get_files(root):
    files_list = []
    for subdir, dirs, files in os.walk(root):
        for file in files:
            files_list.append(os.path.join(subdir, file))
    return files_list        

if __name__ == '__main__':
    files =  []
    root = sys.argv[1]
    files = get_files(root) 
    for file1, file2 in itertools.combinations(files,2):
        if (are_files_duplicates(file1,file2)):
            print("Файл {} есть в папке {}".format(file1,file2))

    

