class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COLS= len(matrix),len(matrix[0])

        Top , bot=0, ROW-1
        while Top <= bot:
            row= (Top+bot)//2
            if target > matrix[row][-1]:
                top= row+1
            elif target < matrix[row][0]:
                top=row-1
            else:
                break
        
        if not (Top <= bot):
            return False
        row= (Top+bot)//2
        l,r=0,COLS-1
        mid=(l+r)//2
        if target >matrix[row][mid]:
            l=mid+1
        elif target <matrix[row][mid]:
            r=mid-1
        else:
            return True
    return False
        
        
        

        
        
        
        

        
        
        
        