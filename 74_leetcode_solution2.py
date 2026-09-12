class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return(target in row for row in matrix)
    
    

