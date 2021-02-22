from os import path
from sys import exit

"""
cultural_names = {
    pictish = cn_pictavia
    irish = cn_alba
    gaelic = cn_alba
}

Should become:
cultural_names = {
    pictish = cn_pictavia
    irish = cn_alba
    gaelic = cn_alba
    welsh = cn_alba 
}
"""


def main(file_path: str, original_name: str, new_name: str):
    """
    :param file_path: Path of file to be scanned and updated
    :param original_name: Name to be matched
    :param new_name: Name to appear in the new line, in place of the original name
    :return The number of occurrences of original_name that have been found
    """
    print('Scanning file...')

    new_lines = []
    occurrences = 0
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line)
            if original_name in line.split():
                occurrences += 1
                line = line.replace(original_name, new_name)
                new_lines.append(line)

    print(f'Found {occurrences} occurrences of {original_name} in file {file_path}')

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

    print(f'Added {occurrences} occurrences of {new_name} in file {file_path}')
    return occurrences


def args():
    """
    Validates the command line arguments and returns them
    """
    file_path = input('File to scan and update: ')
    if not file_path:
        exit('Name must not be empty')
    if not path.isfile(file_path):
        exit(f'File {file_path} does not exist')

    original_name = input('Original name: ')
    if not original_name:
        exit('Name must not be empty')

    new_name = input('New name: ')
    if not original_name:
        exit('Name must not be empty')

    return file_path, original_name, new_name
