def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    fresh = 0;

    # with open('input_test.txt', 'r', encoding='utf-8') as file:
    #     input = file.read()

    data = input.split("\n\n");
    ranges = data[0].split("\n");

    # create tuples for ranges
    ranges = [tuple(map(int, range.split("-"))) for range in ranges];   
    
    # sort the ranges
    ranges.sort(key=lambda x: x[0]);

    # split the ranges into two arrays, one for the lower bounds and one for the upper bounds
    lower_bounds = [range[0] for range in ranges];
    upper_bounds = [range[1] for range in ranges];

    print(lower_bounds, upper_bounds);

    max_upper = 0;

    # iterate through array and find the 
    for i in range(len(lower_bounds)):
        ingredients = 0;

        if (i == 0):
            ingredients = upper_bounds[i] - lower_bounds[i] + 1;
            max_upper = upper_bounds[i];
        # if seen entirely new range, add the number of ingredients to the fresh count
        elif lower_bounds[i] > max_upper:
            ingredients =  upper_bounds[i] - lower_bounds[i] + 1;
            max_upper = upper_bounds[i];
        elif upper_bounds[i] > max_upper:
            ingredients =  upper_bounds[i] - max_upper;
            max_upper = upper_bounds[i];

        fresh += ingredients;

    print(fresh);

main();