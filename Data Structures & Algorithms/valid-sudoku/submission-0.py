class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            nums_arr = []
            for j in range(9):
                nums_arr.append(board[i][j])
            if self.containsDuplicate(nums_arr):
                return False
        
        for j in range(9):
            nums_arr = []
            for i in range(9):
                nums_arr.append(board[i][j])
            if self.containsDuplicate(nums_arr):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums_arr = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        nums_arr.append(board[i][j])
                if self.containsDuplicate(nums_arr):
                    return False
        
        return True
    
    def containsDuplicate(self, nums: List[str]) -> bool:
        num_map = {}
        for num in nums:
            if num == ".":
                continue
            if num in num_map:
                return True
            else:
                num_map[num] = num
        return False