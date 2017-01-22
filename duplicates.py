import os
import itertools
import filecmp
import sys

def are_files_duplicates(file_path1,file_path2):
    duplicate = filecmp.cmp(file_path1,file_path2)
    return  duplicate    

def get_files(root):
    files_list = []
    for subdir, dirs, files in os.walk(root):
        for file in files:
            files_list.append(os.path.join(subdir, file))
    return files_list        

if __name__ == '__main__':
    root = sys.argv[1]

    files = get_files(root) 
    for file1, file2 in itertools.combinations(files,2):
        if (are_files_duplicates(file1,file2)):
            print("Файл {} имеет дубль {}".format(file1,file2))

    

