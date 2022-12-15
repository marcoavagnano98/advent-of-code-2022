if __name__ == '__main__':
    from operator import itemgetter
    import heapq

    elfs = {}
    ind = 0
    with open("first/input.txt", "r") as fl:
        for line in fl:
            key = str(ind)
            if not line.isspace():
                if not key in elfs:
                    elfs[str(ind)] = int(line.strip())
                else:
                    elfs[str(ind)] += int(line.strip())
            else:
                ind += 1
    print(f'ELFS MAX CALORIES: {max(elfs.values())}')
    elfs_tuple = heapq.nlargest(3, elfs.items(), key=itemgetter(1))
    calories_sum = 0
    for key, value in elfs_tuple:
        calories_sum += value
    print(elfs_tuple[0][1])
    print(f'TOP THREE ELFS CALORIES:{elfs_tuple}, SUM: {calories_sum}')
