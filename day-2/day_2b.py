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
        midway = math.floor(len(str(i)) / 2);
        length_of_i = len(str(i));

        # iterate over all the possible leading digits i.e. 1, 12, 123
        for j in range(1, midway + 1):
            leading_digits = str(i)[:j];

            # calculate how many times the repeating number can fit
            if length_of_i % j == 0:
                no_repetitions = length_of_i // j;
                repeating_number = int(str(leading_digits) * no_repetitions);
                if repeating_number in visited:
                    continue;
                visited.add(repeating_number);
                if repeating_number in range(start, end + 1):
                    res += repeating_number;

print (res);