import math;

with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read()

banks = input.split("\n");
res = 0;

for bank in banks:
    jolts = [int(i) for i in str(bank)];

    left = 0;
    index = 0;

    # find the left-most maximum value in the bank that is not the last
    for i in range(0, len(jolts) - 1):
        if jolts[i] > left:
            left = jolts[i];
            index = i;

    # split the array to the right of the left-most maximum value
    jolts_right = jolts[index + 1:];
    right = max(jolts_right);

    res += int(str(left) + str(right));

    # find the maximum value that is not the last number in the array

print (res);