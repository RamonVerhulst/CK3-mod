from os import path
from sys import exit


def main(file_path: str, first_item: str, second_item: str):
    """
    :param file_path: Path of file to be scanned and updated
    :param first_item: First item to be matched
    :param second_item: Second item to be matched
    :return The number of lines that have been deleted
    """
    print('Scanning file...')

    new_lines = []
    occurrences = 0
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            splitted = line.split()
            if first_item in splitted and second_item in splitted:
                # Don't add this line, but simply count the line as deleted
                occurrences += 1
            else:
                new_lines.append(line)

    print(f'Found {occurrences} lines containing {first_item} and {second_item} in file {file_path}')

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

    print(f'Deleted {occurrences} lines containing {first_item} and {second_item} from file {file_path}')
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

    first_item = input('First item: ')
    if not first_item:
        exit('Item must not be empty')

    second_item = input('Second item: ')
    if not second_item:
        exit('Item must not be empty')

    return file_path, first_item, second_item
