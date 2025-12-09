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
        script_line = re.split(r'\s+', list[i].strip());
        script[i] = script_line;
    
    columns = [[0 for _ in range(len(list))] for _ in range(len(script[0]))];
    
    # create columns
    for i in range(len(script[0])):
        columns[i] = [script[j][i] for j in range(len(script))];
    
    res = 0;

    operation_index = len(list) - 1;

    # loop through all columns
    for i in range(len(columns)):
        # find the longest string size in the column
        longest = len(max(columns[i], key=len));

        # create an empty list with size of longest string to create ints
        new_numbers = ['' for _ in range(longest)];

        # loop through the rows of each script and detach length of longest + 1 (to account for space)
        for j in range(len(list) - 1):
            number = str(list[j][:longest + 1]);
            list[j] = list[j][longest + 1:];

            # distribute the numbers into the new list
            for k in range(0, len(number)):
                if (number[k] == ' '):
                    continue;
                new_numbers[k] = str(new_numbers[k]) + str(number[k]);
                


        # convert new numbers to ints
        new_numbers = [int(x) for x in new_numbers];

        if columns[i][operation_index] == "*":
            res += math.prod(new_numbers);
        elif columns[i][operation_index] == "+":
            res += sum(new_numbers);
        
    print(res);

main();