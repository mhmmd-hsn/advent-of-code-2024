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


for row in data:
    is_increasing = all(row[i] < row[i+1] for i in range(len(row)-1))
    is_decreasing = all(row[i] > row[i+1] for i in range( len(row)-1))
    if is_increasing or is_decreasing:
        safe_sequence = all(1 <= abs(row[i] - row[i+1]) <= 3 for i in range(len(row)-1))
        if safe_sequence:
            safe += 1
    
print(safe)