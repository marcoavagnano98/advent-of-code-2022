if __name__ == '__main__':
    line = open("sixth/input.txt", "r").readline()
    line = line.strip()
    counter = 0
    distinct_char = 14
    while True:
        if len(set([c for c in line[counter: counter + distinct_char]])) == distinct_char:
            break
        counter += 1
    print(counter + distinct_char)  # final position
