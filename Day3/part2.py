def calculate_enabled_multiplications_sum(text):
    import re
    
    total_sum = 0
    mul_enabled = True  
    
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    instructions = []
    
    for match in re.finditer(mul_pattern, text):
        num1, num2 = int(match.group(1)), int(match.group(2))
        instructions.append(('mul', match.start(), num1, num2))

    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start()))
    

    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start()))
    
    instructions.sort(key=lambda x: x[1])
    

    for instruction in instructions:
        if instruction[0] == 'do':
            mul_enabled = True
        elif instruction[0] == 'dont':
            mul_enabled = False
        elif instruction[0] == 'mul' and mul_enabled:
            num1, num2 = instruction[2], instruction[3]
            total_sum += num1 * num2
    
    return total_sum

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return calculate_enabled_multiplications_sum(content)


file_path = "Day3/data.txt"  
result = process_file(file_path)
print(f"Sum of enabled multiplications: {result}")