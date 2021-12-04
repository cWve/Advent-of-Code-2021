increased_count = 0
with open("input.txt",'r') as file:
    first_number = int(file.readline())
    for line in file:
        second_number = int(line)
        if second_number > first_number:
            increased_count += 1
        first_number = second_number

print(increased_count)
