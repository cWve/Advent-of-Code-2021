#12
bits = 12
counters = [0 for i in range(bits)]
line_count = 0
with open("input.txt",'r') as file:
    for line in file:
        line_count += 1
        for i,digit in enumerate(line.rstrip()):
            counters[i] += int(digit)

gamma = 0
epsilon = 0
for i,total in enumerate(counters):
    if total > int(line_count/2): #More 1s than 0s
        gamma += 2**(bits-1-i)
    else:
        epsilon += 2**(bits-1-i)
print(f"gamma = {gamma} epsilon = {epsilon}")
print(f"Power = {gamma * epsilon}")




