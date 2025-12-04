def remove_scroll(grid):
    reachable = 0;

    # iterate in a 3x3 sliding window
    for i in range(0, len(grid) - 2):
        for j in range(0, len(grid[0]) - 2):
            scrolls = 0;
            # count the number of '@' in the 3x3 window
            for k in range(0, 3):
                for l in range(0, 3):
                    if k == 1 and l == 1:
                        continue;
                    if grid[i + k][j + l] == '@':
                        scrolls += 1;
            
            
            if scrolls < 4 and grid[i + 1][j + 1] == '@':
                reachable += 1;
    
    return reachable;

def main():
    with open('input_test.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    grid = input.split("\n");

    # pad grid with '.'
    grid = ['.' + row + '.' for row in grid]
    grid = ['.' * len(grid[0])] + grid + ['.' * len(grid[0])]

    # print the grid
    for row in grid:
        print(row);

    
    reachable = remove_scroll(grid);

    print(reachable);

main();