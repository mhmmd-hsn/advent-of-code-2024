
output = 0
with open("Day3/data.txt", 'r') as file:
    for line in file:
        if line.strip(): 
            import re
            numbers = re.findall(r'mul\((\d+),(\d+)\)', line)
            if numbers:
                for num1, num2 in numbers:
                    output += int(num1)*int(num2)

print(output)
