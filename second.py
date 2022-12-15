winner_dicts = {"A": "Y", "B": "Z", "C": "X"}
looser_dicts = {"A": "Z", "B": "X", "C": "Y"}
eq_dict = {"A": "X", "B": "Y", "C": "Z"}


# first part
def get_points(pred, move):
    # draw
    if move == eq_dict[pred]:
        return 3 + get_point_for_elem(move)
    # win or loss
    return 6 + get_point_for_elem(move) if move == winner_dicts[pred] else 0 + get_point_for_elem(move)


# second part
def get_point_for_elem(elem):  # Rock X, Paper Y, Scissor Z
    if elem == "X":
        return 1
    if elem == "Y":
        return 2
    if elem == "Z":
        return 3
    return 0


def choose_round_end(pred, move):
    new_move = ""
    if move == "X":
        new_move = looser_dicts[pred]
    if move == "Y":
        new_move = eq_dict[pred]
    if move == "Z":
        new_move = winner_dicts[pred]
    return get_points(pred, new_move)


if __name__ == '__main__':
    points_p1 = 0
    points_p2 = 0
    with open("second/input.txt", "r") as fl:
        for line in fl:
            stripped_line = line.strip()
            pred = stripped_line[0]
            move = stripped_line[2]
            points_p1 += get_points(pred, move)
            points_p2 += choose_round_end(pred, move)
    print(f'POINTS PART1:{points_p1}, POINTS PART2:{points_p2}')
