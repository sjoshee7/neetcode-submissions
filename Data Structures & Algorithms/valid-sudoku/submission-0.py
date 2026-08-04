class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_ind = (r // 3) * 3 + (c // 3)
                if val == '.':
                    continue
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[box_ind]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_ind].add(val)
                # check row, col, box for duplicates
                # if duplicate found anywhere, return False
                # otherwise, add val to the appropriate row/col/box set
        
        return True