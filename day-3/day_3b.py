def find_maximum(jolts, search_size, max_jolt):
    # if the search size is 0 we are done
    if search_size == 0:
        return max_jolt;
    
    # if the search size is the same as the length of the array, we can return the max_jolt plus the array joined together
    if search_size == len(jolts):
        return max_jolt + ''.join(str(j) for j in jolts);

    digit = 0;
    index = 0;
    
    # find the left-most maximum value in the bank that is not in the last search_size elements
    for i in range(0, len(jolts) - search_size + 1):

        if jolts[i] == 9: # highest value, we can skip the rest of the array
            digit = 9
            index = i;
            break;

        if jolts[i] > digit:
            digit = jolts[i];
            index = i;

    # split the array to the right of the left-most maximum value
    jolts = jolts[index + 1:];
    search_size -= 1;
    max_jolt += str(digit);

    return find_maximum(jolts, search_size, max_jolt);

def main():
    res = 0;

    with open('input.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    banks = input.split("\n");

    for bank in banks:
        
        jolts = [int(i) for i in str(bank)];
        search_size = 12;

        jolt = find_maximum(jolts, search_size, "");

        print(jolt);

        res += int(jolt);

    print(res);

main();