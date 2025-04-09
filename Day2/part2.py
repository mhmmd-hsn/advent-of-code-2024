filename = 'Day2/numbers.txt'
data = []
safe = 0
with open(filename, 'r') as f:
    for line in f:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        parts = cleaned_line.split()
        row_of_numbers = [int(part) for part in parts]
        data.append(row_of_numbers)

def is_safe(levels):
    if len(levels) <= 1:
        return True
        
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    if not (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)):
        return False
    return all(1 <= abs(diff) <= 3 for diff in differences)

def is_safe_with_dampener(levels):

    if is_safe(levels):
        return True
        
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False


print(sum(is_safe_with_dampener(data) for data in data))