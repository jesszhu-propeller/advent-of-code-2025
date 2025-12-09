import re
import math

def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    # with open('input_test.txt', 'r', encoding='utf-8') as file:
    #     input = file.read()

    list = input.split("\n");

    # initialise 2D array the size of the list
    script = [[0 for _ in range(len(list))] for _ in range(len(list))];

    for i in range(len(list)):
        if i == len(list) - 1:
            script_line = re.split(r'\s+', list[i].strip());
        else:
            script_line = [int(x) for x in re.split(r'\s+', list[i].strip())];

        script[i] = script_line;
    
    operation_index = len(list) - 1;
    entries = len(script[0]);

    res = 0;

    for i in range(entries):
        print(script[operation_index][i]);
        if script[operation_index][i] == "*":
            # multiply the entries in the column
            total = 1;
            for j in range(operation_index):
                total *= script[j][i];
            res += total;
        elif script[operation_index][i] == "+":
            # add the entries in the column
            total = 0
            for j in range(operation_index):
                total += script[j][i];
            res += total;

    print(res);

main();