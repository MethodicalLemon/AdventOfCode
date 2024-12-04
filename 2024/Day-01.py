#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Day 1 of Advvent of Code
Author: MethodicalLemon
Date: 01/12/2024
"""

import argparse
from collections import Counter


def process_input(file):
    """
    Take the input from Advent of Code and turn it into two lists
    """
    a = []
    b = []
    with open(file, "r") as fh:
        for line in fh.readlines():
            # print(line)
            line = line.strip()
            a.append(int(line.split("   ")[0]))
            b.append(int(line.split("   ")[1]))

    return a, b


def sum_element_wise_diff(a, b):
    """
    Order the lists, and find the sum of the differences between each pair.
    """
    a = sorted(a)
    b = sorted(b)
    diffs = [abs(a - b) for a, b in zip(a, b)]

    return sum(diffs)


def score_similarity(a, b):
    """
    Calculate a total similarity score by adding up each number
    in the left list after multiplying it by the number of times
    that number appears in the right list.
    """
    b_freq = Counter(b)

    counts_of_a_in_b = [b_freq[i] for i in a]
    scores = [x * y for x, y in zip(a, counts_of_a_in_b)]

    return sum(scores)


def main():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument("input", help="Input file path")
    args = parser.parse_args()

    lista, listb = process_input(args.input)

    # Day 1
    day1_part1_answer = sum_element_wise_diff(lista, listb)

    print(f"Day 01 - part 1 answer: {day1_part1_answer}")

    day1_part2_answer = score_similarity(lista, listb)

    print(f"Day 01 - part 2 answer: {day1_part2_answer}")

    # Day 2


if __name__ == "__main__":
    main()
