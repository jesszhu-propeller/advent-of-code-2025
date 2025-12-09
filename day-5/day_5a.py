def func():
    return 0;

def main():
    # with open('input.txt', 'r', encoding='utf-8') as file:
    #     input = file.read()

    reachable = 0;

    with open('input_test.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    grid = input.split("\n");

    for row in grid:
        print(row);

    print(reachable);

main();