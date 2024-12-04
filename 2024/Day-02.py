#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Day 2 of Advvent of Code
Author: MethodicalLemon
Date: 02/12/2024
"""

import argparse


def process_input(input):
    """
    Take the input from Advent of Code and turn it into a list of integer lists
    """
    lst = []
    with open(input, "r") as fh:
        for line in fh.readlines():
            readings = line.strip().split()
            ints = [int(e) for e in readings]
            lst.append(ints)

    return lst


def check_safety(report):
    if sorted(report) == report or sorted(report) == list(reversed(report)):
        # trend is okay but need to check for jumps between values
        deltas = []
        for i in range(len(report) - 1):
            deltas.append(abs(report[i] - report[i + 1]))
        if min(deltas) > 0 and max(deltas) < 4:
            return True
        else:
            return False
    else:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    # Common setup
    reports = process_input(args.input)

    # Part 1
    counter = 0

    for report in reports:
        counter += check_safety(report)

    print(f"Day 02 - part 1 answer: {counter}")

    # Part 2 - Reset counter
    counter = 0

    for report in reports:
        for i in range(len(report)):
            permutation = [elem for j, elem in enumerate(report) if j != i]
            print(f"{permutation} : {check_safety(permutation)}")
            if check_safety(permutation):
                counter += 1
                break

    print(f"Day 02 - part 2 answer: {counter}")


if __name__ == "__main__":
    main()
