"""https://adventofcode.com/2024/day/2"""

# part 1

def is_safe(report):
    direction = []  # booleans to represent increasing or decreasing levels

    for i in range(0, len(report) - 1):
        if 0 < abs(report[i] - report[i + 1]) <= 3:
            direction.append(report[i] < report[i + 1])
        else:
            return False

    # a single element set indicates consistent direction
    return True if len(set(direction)) == 1 else False

reports = []

with open("2.input", encoding="utf-8") as lines:
    for line in lines:
        reports.append([int(x) for x in line.split()])

safe = []
unsafe = []

for report in reports:
    if is_safe(report):
        safe.append(report)
    else:
        unsafe.append(report)

print(len(safe))
assert len(safe) == 213

# part 2

tolerable = []

for report in unsafe:
    for i in range(len(report)):
        dup = report[:]
        dup.pop(i)
        if is_safe(dup):
            tolerable.append(report)
            break

print(len(safe) + len(tolerable))
assert len(safe) + len(tolerable) == 285
