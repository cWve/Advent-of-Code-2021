xpos = 0
ypos = 0
aim = 0
with open('input.txt','r') as file:
    for line in file:
        words = line.split(' ')
        direction = words[0]
        number = int(words[1])
        if direction == 'forward':
            xpos += number
            ypos += aim*number
        elif direction == 'up':
            aim -= number
        elif direction == 'down':
            aim += number
        else:
            print("Something went wrong parsing")
            exit(1)
        print(f"Direction: {direction}, Number: {number}")
    print(f"Total xpos:{xpos}, ypos:{ypos}\n f:{xpos*ypos}")
