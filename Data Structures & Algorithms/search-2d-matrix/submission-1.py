class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                curr_left = 0
                curr_right = len(matrix[mid]) - 1
                while curr_left <= curr_right:
                    curr_mid = (curr_left + curr_right) // 2
                    if target > matrix[mid][curr_mid]:
                        curr_left = curr_mid + 1
                    elif target < matrix[mid][curr_mid]:
                        curr_right = curr_mid - 1
                    else:
                        return True
                return False
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1

        return False