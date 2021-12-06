#x1 y1  x2 y2
#0,9 -> 5,9
NCol = 10
NRow = 10
grid = [ [ 0 for i in range(NRow)] for j in range(NCol) ]

#Parsing
with open("sample.txt",'r') as file:
    for line in file:
        tokens = line.rstrip().split(' ')
        x1, y1 = map(int,tokens[0].split(','))
        x2, y2 = map(int,tokens[2].split(','))

#Drawing
#Horizontal: x2-x1 = 0
#Vertical: y2-y1 = 0
#Diagonal y2-y1 = x2-x1
        print(x1,y1,x2,y2)
        diffx = x2-x1
        diffy = y2-y1
        if diffx == 0:
            for j in range(y1,y2+1,diffy//abs(diffy)):
                grid[j][x1] += 1
        elif diffy == 0:
            for i in range(x1,x2+1,diffx//abs(diffx)):
                grid[y1][i] += 1

#Printing
overlap_count = 0
for i in range(NRow):
    for j in range(NCol):
        val = grid[i][j]
        if val == 0:
            val = '.'
        elif val >= 2:
            overlap_count += 1
        print(val,end="")
    print()
print(overlap_count)



