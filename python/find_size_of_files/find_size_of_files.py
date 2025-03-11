import os
import re

# Нужно написать скрипт, который выводит сумму размеров всех файлов в гигабайтах, которые начинаются с Logs или logs и имеют расширение .ibd в текущей директории. Результат округлить до целого числа
def find_required_file_paths(absolute_directory_path):
    regex = re.compile(r"^(Logs)|(logs).+\.ibd$")
    tree = os.walk(absolute_directory_path)
    matched_files = []
    for root, _, files in tree:
        for file in files:
            if regex.search(file):
                full_file_path = os.path.join(root, file)
                matched_files.append(full_file_path)
    return matched_files

def find_sum_of_file_sizes(file_paths):
    sum = 0
    for file in file_paths:
        sum += os.path.getsize(file)
    return sum

def convert_bytes_to_gigabytes(number):
    return number / (1000^3)

if __name__ == "__main__":
    file_paths = find_required_file_paths(".")
    print(f"Found the following files that match requirements: {file_paths}")
    sum_of_sizes_in_bytes = find_sum_of_file_sizes(file_paths)
    sum_of_sizes_in_gigabytes = convert_bytes_to_gigabytes(sum_of_sizes_in_bytes)
    print(f"Sum of .ibd log files in GB: {sum_of_sizes_in_gigabytes:.0f}")
