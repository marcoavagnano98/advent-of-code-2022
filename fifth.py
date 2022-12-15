if __name__ == '__main__':
    CrateMover9000 = [["Q", "W", "P", "S", "Z", "R", "H", "D"],
                      ["V", "B", "R", "W", "Q", "H", "F"],
                      ["C", "V", "S", "H"],
                      ["H", "F", "G"],
                      ["P", "G", "J", "B", "Z"],
                      ["Q", "T", "J", "H", "W", "F", "L"],
                      ["Z", "T", "W", "D", "L", "V", "J", "N"],
                      ["D", "T", "Z", "C", "J", "G", "H", "F"],
                      ["W", "P", "V", "M", "B", "H"]]

    import copy
    CrateMover9001 = copy.deepcopy(CrateMover9000)
    with open("fifth/input.txt", "r") as fl:
        for line in fl.readlines():
            s_line = line.strip().split(' ')
            n = int(s_line[1])
            start = int(s_line[3]) - 1
            end = int(s_line[5]) - 1
            CrateMover9000[end] += reversed(CrateMover9000[start][-n:])
            CrateMover9001[end] += CrateMover9001[start][-n:]
            del CrateMover9000[start][-n:]
            del CrateMover9001[start][-n:]
        str9000 = ''.join([crave[-1] for crave in CrateMover9000])
        str9001 = ''.join([crave[-1] for crave in CrateMover9001])
        print(f'CreateMover9000: {str9000}, CreateMover9001:{str9001}')
