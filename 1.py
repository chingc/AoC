"""https://adventofcode.com/2024/day/1"""

# part 1

left = []
right = []

with open("1.input", encoding="utf-8") as lines:
    for line in lines:
        x, y = line.split()
        left.append(int(x))
        right.append(int(y))

left.sort()
right.sort()

diffs = [abs(x - y) for x, y in zip(left, right)]
distance = sum(diffs)

print(distance)
assert distance == 1110981

# part 2

frequency = {}  # key: number, value: [freq in left, freq in right]

for x in left:
    if x in frequency:
        frequency[x][0] += 1
    else:
        frequency[x] = [1, 0]

for x in right:
    if x in frequency:
        frequency[x][1] += 1

similarity = 0

for k, v in frequency.items():
    if v[1] == 0:
        continue
    score = k * v[1]
    if v[0] > 1:
        score *= v[0] + 1
    similarity += score

print(similarity)
assert similarity == 24869388
