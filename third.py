lower_min = ord('a')
upper_min = ord('A')


def get_priority(c):
    i_value = ord(c)
    if c.isupper():
        return (i_value - upper_min) + 1 + 26
    return (i_value - lower_min) + 1


def get_badge(lines):
    return ''.join(set(lines[0]).intersection(lines[1]).intersection(lines[2]))


if __name__ == '__main__':
    with open("third/input.txt", "r") as fl:
        total_priorities = 0
        badge_priorities = 0
        badge_lines = []
        for line in fl:
            s_line = line.strip()
            split_len = int(len(s_line) / 2)
            badge_lines.append(s_line)
            if len(badge_lines) == 3:  # second part
                badge_priorities += get_priority(get_badge(badge_lines))
                badge_lines = []
            for c in set(s_line[:split_len]).intersection(s_line[split_len:]):
                total_priorities += get_priority(c)
        print(f'TOTAL PRIORITIES: {total_priorities}, BADGE PRIORITIES: {badge_priorities}')
