def count_of_pairs(pairs):
    tribes = [set(pairs[0])]
    count = 0

    for pair in pairs[1:]:
        for tribe in tribes:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                break
            else:
                tribes.append(set(pair))

    for i in range(len(tribes)):
        for j in range(i + 1, len(tribes)):
            for first_person in tribes[i]:
                for second_person in tribes[j]:
                    if first_person % 2 != second_person % 2:
                        count += 1

    return count


def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        N = int(lines[0])
        pairs = [tuple(map(int, line.split())) for line in lines[1:]]

    return N, pairs


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


def main(input_filename, output_filename):
    N, pairs = read_input(input_filename)

    result = count_of_pairs(pairs)
    write_output(output_filename, result)


if __name__ == "__main__":
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    main(input_filename, output_filename)
