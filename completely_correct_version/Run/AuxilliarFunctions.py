import os

def take_requirements(requ_name, path_to_requ):
    os.chdir(path_to_requ)
    not_have = []
    have = []
    command = []
    file = open(requ_name, "r")
    a = file.readline()
    while a != '':
        arr = a.split(':')
        if "Must not have" in arr[0]:
            not_have.append(arr[1])
        if "Must have" in arr[0]:
            have.append(arr[1])
        if "Command" in arr[0]:
            command.append(arr[1][:len(arr[1]) - 1])
        a = file.readline()
    return [not_have, have, command]

def is_variable(line):
    if len(line)<1:
        return False
    if 'return' in line:
        return False
    if '(' in line:
        return False
    if 'int' in line:
        return True

    return False