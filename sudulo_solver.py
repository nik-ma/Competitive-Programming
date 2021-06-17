board=[]
print('Enter your suduko puzzle')
for i in range(9):
    board.append([int(x) for x in input().split()])
for i in range(9):
    print(board[i])
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            for ni in range(1,10):
                for nik in range(9):
                    if ni==board[i][nik] or ni==board[nik][j]:
                        break
                else:
                    flag=0
                    if i<3 and j<3:
                        
                        for nikh in range(3):
                            for nikh2 in range(3):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i<3 and j>=3 and j<6:
                        for nikh in range(3):
                            for nikh2 in range(3,6):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i<3 and j>=6 and j<9:
                        for nikh in range(3):
                            for nikh2 in range(6,9):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=3 and i<6 and j<3:
                        for nikh in range(3,6):
                            for nikh2 in range(3):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=3 and i<6 and j>=3 and j<6:
                        for nikh in range(3,6):
                            for nikh2 in range(3,6):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=3 and i<6 and j>=6 and j<9:
                        for nikh in range(3,6):
                            for nikh2 in range(6,9):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=6 and i<9 and j<3:
                        for nikh in range(6,9):
                            for nikh2 in range(3):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=6 and i<9 and j>=3 and j<6:
                        for nikh in range(6,9):
                            for nikh2 in range(3,6):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                    elif i>=6 and i<9 and j>=6 and j<9:
                        for nikh in range(6,9):
                            for nikh2 in range(6,9):
                                if ni==board[nikh][nikh2]:
                                    flag=1
                                    break
                            if flag!=0:
                                break
                        if flag!=1:
                            board[i][j]=ni
                        else:
                            print('Here comes backtracking')                            
print(' not happening now')
for i in range(9):
    print(board[i])


