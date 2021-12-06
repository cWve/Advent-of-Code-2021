#Parsing
NCol = 5
NRow = 5
with open("input.txt",'r') as file:
    drawn_nums = [ int(num) for num in file.readline().split(',') ]
    print(drawn_nums)
    
    boards = [] #List containing board_nums
    board_nums = [] # 2D Array
    for line in file:
        if line == '\n':
            board_nums = [] # 2D Array
            for i in range(NRow):
                line = file.readline()
                board_nums.append([ int(num) for num in line.split() ])
            print(board_nums)
        else:
            print("I'm not suppossed to reach this place!")

        boards.append(board_nums)
    print(f"\n{boards}")
#End parsing

def mark_board(board_num, num):
    modified = False
    for i in range(NRow):
        for j in range(NCol):
            if board_num[i][j] == num:
                board_num[i][j] = -1
                modified = True
                return modified, board_num, i, j

    return modified, board_num, i, j


def check_board(board_num, iX,jX):
    #Check column
    winnerRow = True
    winnerColumn = True
    for k in range(NCol):
        if board_num[iX][k] != -1:
            winnerColumn = False
            
    for k in range(NRow):
        if board_num[k][jX] != -1:
            winnerRow = False
    return winnerRow or winnerColumn


for num in drawn_nums:
    for i in range(len(boards)):
        if num == 24 and i == 2:
            print("apu")
        modified, boards[i], iX, jX = mark_board(boards[i],num)
        if modified:
            print(num,boards[i])
            if check_board(boards[i], iX, jX):

                score = 0
                for j in range(NRow):
                    for k in range(NCol):
                        if boards[i][j][k] != -1:
                            score += boards[i][j][k]
                score *= num
                print(f"Winner: {boards[i]}")
                print(f"Score: {score}")
                exit(0)

        
# 2D (N*M) --> 1D  [a][b] --> [M*(a-1) + (b-1)]
# [2][1] --> 5*1 + 0 = 5

