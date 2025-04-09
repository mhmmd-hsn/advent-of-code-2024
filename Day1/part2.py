filename = 'Day1/numbers.txt'

column1 = []
column2 = []

with open(filename, 'r') as f:
    for line in f:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        parts = cleaned_line.split()
        if len(parts) == 2:
            column1.append(int(parts[0]))
            column2.append(int(parts[1]))

column1.sort()
column2.sort()

total_similarity = 0
for i in range(len(column1)):
    total_similarity += column1[i] * column2.count(column1[i])

print(total_similarity)