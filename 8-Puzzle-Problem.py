from collections import deque

class Solution:
    def solve(self, board):
        
        start = tuple(sum(board, []))  
        target = (0, 1, 2, 3, 4, 5, 6, 7, 8)  
        moves = {  
            0: [1, 3], 
            1: [0, 2, 4], 
            2: [1, 5], 
            3: [0, 4, 6], 
            4: [1, 3, 5, 7], 
            5: [2, 4, 8],
            6: [3, 7], 
            7: [4, 6, 8], 
            8: [5, 7]
        }
        
        queue = deque([(start, 0)])  
        visited = {start}  
        
        while queue:
            cur, steps = queue.popleft()  
            
            if cur == target: 
                return steps
            
            zero = cur.index(0)
            
            for move in moves[zero]:
                nxt = list(cur)  
                nxt[zero], nxt[move] = nxt[move], nxt[zero]  
                nxt = tuple(nxt)  
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))  
        
        return -1

ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("NO OF MOVES==", ob.solve(matrix))