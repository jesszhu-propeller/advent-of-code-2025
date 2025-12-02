import math;

with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read()

ids = input.split(",");
res = 0;

for id in ids:
    id_range = id.split("-");
    start = int(id_range[0]);
    end = int(id_range[1]);

    visited = set();

    for i in range(start, end + 1):
        # if the number has an odd number of digits, skip
        if len(str(i)) % 2 == 1:
            continue;
        else:
            # split the number into two halves
            leading_digits = str(i)[:len(str(i)) // 2];
            if leading_digits in visited:
                continue;
            visited.add(leading_digits);
            repeating_number = int(str(leading_digits) + str(leading_digits));
            if repeating_number in range(start, end):
                res += repeating_number;

print (res);