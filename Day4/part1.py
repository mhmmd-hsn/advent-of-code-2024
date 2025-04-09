def count_xmas_occurrences(grid):
    """
    Count occurrences of 'XMAS' in all directions in the given grid.
    
    Args:
        grid (list): List of strings representing the word search grid
        
    Returns:
        int: Total number of 'XMAS' occurrences
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Define the 8 possible directions
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    # Check each starting position
    for r in range(rows):
        for c in range(cols):
            # Try each direction from this position
            for dr, dc in directions:
                # Check if 'XMAS' can fit in this direction
                if (0 <= r + 3*dr < rows and 0 <= c + 3*dc < cols):
                    # Check if 'XMAS' is found in this direction
                    if (grid[r][c] == 'X' and 
                        grid[r+dr][c+dc] == 'M' and 
                        grid[r+2*dr][c+2*dc] == 'A' and 
                        grid[r+3*dr][c+3*dc] == 'S'):
                        count += 1
    
    return count

def parse_grid(input_text):
    """Parse the input text into a grid of characters."""
    return [line.strip() for line in input_text.strip().split('\n') if line.strip()]

def visualize_xmas_occurrences(grid):
    """
    Create a new grid that only shows letters involved in XMAS occurrences.
    
    Args:
        grid (list): List of strings representing the word search grid
        
    Returns:
        list: List of strings showing only letters involved in XMAS occurrences
    """
    if not grid or not grid[0]:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a grid to track positions involved in XMAS
    tracked_positions = [[False for _ in range(cols)] for _ in range(rows)]
    
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    # Mark positions that are part of XMAS
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if (0 <= r + 3*dr < rows and 0 <= c + 3*dc < cols):
                    if (grid[r][c] == 'X' and 
                        grid[r+dr][c+dc] == 'M' and 
                        grid[r+2*dr][c+2*dc] == 'A' and 
                        grid[r+3*dr][c+3*dc] == 'S'):
                        tracked_positions[r][c] = True
                        tracked_positions[r+dr][c+dc] = True
                        tracked_positions[r+2*dr][c+2*dc] = True
                        tracked_positions[r+3*dr][c+3*dc] = True
    
    # Create a new grid with only the marked positions
    result = []
    for r in range(rows):
        row = ''.join(grid[r][c] if tracked_positions[r][c] else '.' for c in range(cols))
        result.append(row)
    
    return result


# Parse the example input
example_grid = parse_grid(example_input)

# Count XMAS occurrences
example_count = count_xmas_occurrences(example_grid)
print(f"XMAS occurs {example_count} times in the example grid.")

# Visualize the occurrences
visualized_grid = visualize_xmas_occurrences(example_grid)
print("\nVisualized XMAS occurrences:")
for row in visualized_grid:
    print(row)

# Validation: The example should have 18 occurrences
assert example_count == 18, f"Expected 18 occurrences, got {example_count}"

# To solve the actual puzzle, the user would need to provide their input
# with open('puzzle_input.txt', 'r') as file:
#     puzzle_input = file.read()
# puzzle_grid = parse_grid(puzzle_input)
# puzzle_count = count_xmas_occurrences(puzzle_grid)
# print(f"XMAS occurs {puzzle_count} times in the puzzle input.")