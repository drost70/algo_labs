import os


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1


def count_cross_pairs(n, pairs):
    boys_set = set()
    girls_set = set()

    for pair in pairs:
        boy, girl = pair
        boys_set.add(boy)
        girls_set.add(girl)

    boys = list(boys_set)
    girls = list(girls_set)

    ds = DisjointSet(len(boys) + len(girls))

    for boy, girl in pairs:
        ds.union(boys.index(boy), len(boys) + girls.index(girl))

    cross_pairs = 0
    possible_pairs = []

    for boy in boys_set:
        for girl in girls_set:
            if boy % 2 == 1 and girl % 2 == 0 and ds.find(boys.index(boy)) != ds.find(len(boys) + girls.index(girl)):
                cross_pairs += 1
                possible_pairs.append(f"{boy}/{girl}")

    return cross_pairs, possible_pairs


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "output.txt")

    with open("input.txt", "r", encoding="utf-8") as file:
        n = int(file.readline())
        pairs = [list(map(int, line.split())) for line in file]

    result, possible_pairs = count_cross_pairs(n, pairs)

    with open(output_file_path, "w") as output_file:
        output_file.write(f"{result} (Можливі пари - {', '.join(possible_pairs)})\n")


if __name__ == "__main__":
    main()
