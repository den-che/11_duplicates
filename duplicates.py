import os
import itertools
import filecmp
import sys
import argparse

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
    parser = argparse.ArgumentParser("Поиск дубликатов")
    parser.add_argument('--path', help='Папка для поиска дубликатов', required=True)
    args = parser.parse_args()
    root = args.path
    if (root):
        files = get_files(root) 
        for file1, file2 in itertools.combinations(files,2):
            if (are_files_duplicates(file1,file2)):
                print("Дублика ты найдены: {}        {}".format(file1,file2))

    

