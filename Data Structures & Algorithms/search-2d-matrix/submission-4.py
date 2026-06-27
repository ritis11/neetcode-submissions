class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(matrix, t):
            l= 0
            r = len(matrix) - 1
            while l<=r:
                mp = int((l+r)/2)
                if t == matrix[mp]:
                    return True
                elif t> matrix[mp]:
                    l=mp+1
                elif t<matrix[mp]:
                    r=mp-1
            return False

        tr = 0
        br = len(matrix) -1 
        while tr<=br:
            row_idx = (tr+br)//2
            if target >= matrix[row_idx][0] and target <= matrix[row_idx][-1]:
                return binary_search(matrix[row_idx], target)
            elif target < matrix[row_idx][0]:
                br = row_idx-1
            elif target > matrix[row_idx][-1]:
                tr = row_idx + 1
        return False
                

        
        
        