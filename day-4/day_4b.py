def remove_scroll(grid):
    reachable = 0;
    removed_scroll_positions = [];

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
                removed_scroll_positions.append((i + 1, j + 1));
    
    # copy grid and update the removed scroll positions
    for position in removed_scroll_positions:
        grid[position[0]][position[1]] = 'x';

    for row in grid:
        print(''.join(row));

    print();

    return reachable, grid;

def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        input = file.read()

    grid = input.split("\n");


    # pad grid with '.'
    grid = ['.' + row + '.' for row in grid]
    grid = ['.' * len(grid[0])] + grid + ['.' * len(grid[0])]
    grid = [list(row) for row in grid]

    # print the grid nicely
    for row in grid:
        print(''.join(row));
    
    print();

    result = 0;

    while True:
        reachable, new_grid = remove_scroll(grid);
        if reachable == 0:
            break;
        else:
            result += reachable;
        grid = new_grid;

    print(result);

main();