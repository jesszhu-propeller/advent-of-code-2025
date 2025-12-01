import math;

with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read()

commands = input.split("\n");

pos = 50;
res = 0;

for command in commands:
    direction = command[0]
    rotation = int(command[1:])

    prev_pos = pos;

    if direction == "R":
        pos = (pos + rotation) % 100;
    elif direction == "L":
        pos = (pos - rotation) % 100;
    
    full_rotations = math.floor(rotation // 100);

    # will pass 0 after rotating (ends up to the right of 0)
    if (direction == "R" and prev_pos > pos and prev_pos != 0):
        res += 1 + full_rotations;
    # will pass 0 after rotating (ends up to the left of 0)
    elif (direction == "L" and prev_pos < pos and prev_pos != 0):
        res += 1 + full_rotations;
    # lands on 0 after rotating (assuming it did not start at 0)
    elif (pos == 0 and prev_pos != 0):
        res += 1 + full_rotations;
    # otherwise, just add the number of rotations
    else:
        res += full_rotations;

print(res);