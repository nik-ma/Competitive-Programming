class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = list(range(1, 10))
        n = 9
        v_sets = [set() for _ in range(n)] 
        h_sets = [set() for _ in range(n)]
        box_sets = [set() for _ in range(n)]
        
        q_list = []
        
        def get_box(r, c):
            R, C = r // 3, c // 3
            return R * 3 + C
        
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    h_sets[r].add(int(board[r][c]))
                    v_sets[c].add(int(board[r][c]))
                    #print(get_box(r, c), r, c)
                    box_sets[get_box(r, c)].add(int(board[r][c]))
                else:
                    q_list.append((r, c))

        found = False
        def backtrack(idx):   
            nonlocal found
            if idx == len(q_list):
                found = True
                return
            
            r, c = q_list[idx]
            box = get_box(r, c)
            for num in nums:
                if num not in h_sets[r] and num not in v_sets[c] and num not in box_sets[box]:
                    h_sets[r].add(num)
                    v_sets[c].add(num)
                    box_sets[box].add(num)
                    board[r][c] = str(num)
                    
                    backtrack(idx + 1)
                    
                    if found:
                        return
                    h_sets[r].remove(num)
                    v_sets[c].remove(num)
                    box_sets[box].remove(num)
                    board[r][c] = '.'
        
        backtrack(0)
        return board