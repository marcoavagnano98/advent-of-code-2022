if __name__ == '__main__':
    dirs = {"/": 0}
    seq_dirs = []
    with open("seventh/input.txt", "r") as fl:
        for line in fl.readlines():
            command = line.strip().split(' ')
            if (command[0]).isnumeric():
                _path = ''
                for dir_path in seq_dirs:
                    _path += dir_path
                    dirs[_path] += int(command[0])
            if "cd" in command:
                if command[2] == "..":
                    del seq_dirs[-1]
                else:
                    seq_dirs.append(command[2])  # append current dir
            if "dir" in command and (not command[1] in dirs):
                dirs[''.join(seq_dirs[:]) + command[1]] = 0
    print(f'Total sum of directories with size < 100000: {sum([v for v in dirs.values() if v <= 100000])}')
    free_space = 70000000 - dirs["/"]
    min_space_to_delete = 30000000 - free_space
    print(f'Min space to free to run update: {min([v for v in dirs.values() if v >= min_space_to_delete])}')
