"""https://adventofcode.com/2024/day/3"""

import re

# part 1

mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
tokens = ""
total = 0

with open("3.input", encoding="utf-8") as f:
    while True:
        token = f.read(1)

        if not token:
            break  # end of file
        else:
            tokens += token

        if found := mul_pattern.search(tokens):
            x, y = map(int, found.groups())
            total += x * y
            tokens = ""

print(total)
assert total == 183788984

# part 2

enabled = True
tokens = ""
total = 0

with open("3.input", encoding="utf-8") as f:
    while True:
        token = f.read(1)

        if not token:
            break  # end of file
        else:
            tokens += token

        if "don't()" in tokens:
            enabled = False
            tokens = ""
            continue

        if "do()" in tokens:
            enabled = True
            tokens = ""
            continue

        if enabled and (found := mul_pattern.search(tokens)):
            x, y = map(int, found.groups())
            total += x * y
            tokens = ""

print(total)
assert total == 62098619
