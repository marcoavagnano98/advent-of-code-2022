import numpy as np


def complete_overlaps(ranges):
    # 0-> maximum values of two pairs are equals
    # 1 -> maximum value of second pairs is bigger than first
    # -1 -> otherwise
    ind = np.argmin([ranges[1], ranges[3]]) - np.argmax([ranges[1], ranges[3]])
    if ind == 0:
        return 1
    if ind == 1:  # change pairs
        ranges = [ranges[2], ranges[3], ranges[0], ranges[1]]
    return 1 if ranges[0] >= ranges[2] else 0


def partial_overlaps(ranges):
    ind = np.argmax(ranges)
    # change pair if the max range value in second pair is bigger than first
    if ind > 1:
        ranges = [ranges[2], ranges[3], ranges[0], ranges[1]]
    # so now I simply check if the max range value of first pair is lower than min value of second pair
    # or min value of first pair is bigger than max value of second pair, otherwise one is partial contained in other
    if ranges[1] < ranges[2] or ranges[0] > ranges[3]:
        return 0
    return 1


if __name__ == '__main__':
    total_pair = 0
    partial_pair = 0
    with open("fourth/input.txt", "r") as fl:
        for line in fl:
            st_line = line.strip()
            ranges = []
            for val in st_line.split(','):
                ranges += (val.split('-'))
            ranges = [eval(i) for i in ranges]
            total_pair += complete_overlaps(ranges)
            partial_pair += partial_overlaps(ranges)
        print(f'COMPLETE OVERLAPS: {total_pair}, ALL OVERLAPS: {partial_pair}')
