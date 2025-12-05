def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    fresh = 0;

    # with open('input_test.txt', 'r', encoding='utf-8') as file:
    #     input = file.read()

    data = input.split("\n\n");
    ranges = data[0].split("\n");
    ingredients = data[1].split("\n");

    # convert ingredients to integers and sort the ingredients
    ingredients = [int(ingredient) for ingredient in ingredients];
    
    # create tuples for ranges
    ranges = [tuple(map(int, range.split("-"))) for range in ranges];   
    
    # sort the ranges
    ranges.sort(key=lambda x: x[0]);

    for ingredient in ingredients:
        for range in ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                fresh += 1;
                break;

    print(fresh);

main();