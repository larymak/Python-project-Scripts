#!/usr/bin/env python3

import argparse


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ADD = "Add"
REMOVE = "Remove"
IGNORE = "Ignore"

def print_matrix(m1, m2):
    for i in range(len(m1) + 1):
        for j in range(len(m2) + 1):
            print(f"{m1[i][j]}({m2[i][j]})", end=", ")
        print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file1")
    parser.add_argument("file2")
    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2

    with open(file1, 'r') as f:
        file_content1 = f.read()

    with open(file2, 'r') as f:
        file_content2 = f.read()

    lines1 = file_content1.splitlines()
    lines2 = file_content2.splitlines()

    n = len(lines1)
    m = len(lines2)

    distances = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    action = [['0' for _ in range(m + 1)] for _ in range(n + 1)]

    distances[0][0] = 0
    action[0][0] = IGNORE

    for j in range(1, m + 1):
        i = 0
        distances[i][j] = j
        action[i][j] = ADD

    for i in range(1, n + 1):
        j = 0
        distances[i][j] = i
        action[i][j] = REMOVE

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if lines1[i - 1] == lines2[j - 1]:
                action[i][j] = IGNORE
                distances[i][j] = distances[i - 1][j - 1]
                continue

            removeOps = distances[i - 1][j]
            addOps = distances[i][j - 1]

            distances[i][j] = removeOps
            action[i][j] = REMOVE

            if distances[i][j] > addOps:
                distances[i][j] = addOps
                action[i][j] = ADD

            distances[i][j] += 1

    i = n
    j = m
    res = []

    while i > 0 and j > 0:
        _action = action[i][j]
        if _action == IGNORE:
            i -= 1
            j -= 1
        elif _action == ADD:
            j -= 1
            res.append((file2, ADD, j + 1, lines2[j]))
        elif _action == REMOVE:
            i -= 1
            res.append((file1, REMOVE, i + 1, lines1[i]))
        else:
            raise Exception("Unhandled action")

    if not res:
        print(f"{Colors.HEADER}They are the same :){Colors.ENDC}")
        exit(0)

    for (fname, ac, lineno, line) in res:
        if ac == ADD:
            print(fr"{Colors.HEADER}{fname}{Colors.ENDC} | {
                  Colors.OKGREEN}+ {lineno} | {line}{Colors.ENDC}")

        elif ac == REMOVE:
            print(fr"{Colors.HEADER}{fname}{Colors.ENDC} | {
                  Colors.FAIL}- {lineno} | {line}{Colors.ENDC}")


if __name__ == "__main__":
    main()
