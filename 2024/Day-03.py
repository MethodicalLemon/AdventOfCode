#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Day 3 of Advent of Code
Author: MethodicalLemon
Date: 03/12/2024
"""

import argparse
import re


def process_input(file_path):
    with open(file_path, "r") as fh:
        content = fh.read()
        content = content.replace("\n", "")

    return content


def extract_equations_total(string):
    total = 0
    equations = re.findall("mul\((\d+),(\d+)\)", string)
    for values in equations:
        total += int(values[0]) * int(values[1])

    return total


def main():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument("input", help="Input file path")
    args = parser.parse_args()

    text = process_input(args.input)

    total = 0

    total = extract_equations_total(text)

    print(f"Day 03 - part 1 answer: {total}")
    # 187194524

    invalid_strings = re.findall(r"don't\(\).*?(?:do\(\)|$)", text)
    invalid_text = "".join(invalid_strings)
    invalid_total = extract_equations_total(invalid_text)

    print(f"Day 03 - part 1 answer: {total-invalid_total}")
    # 127092535


if __name__ == "__main__":
    main()
