class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
# this class contains functions that are answers for leetcode questions 
class Solution:
    # two binary trees are considered the same if they are identical
    #
    def isSameTree(self, p: Optional[TreeNode], q : Optional[TreeNode]) -> bool: 
        if p == None and q == None : 
            return True 
        elif p == None or q == None:
            return False  
        else : 
            if p.val != q.val :
                return False
                
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range( len (matrix) ):
            if target < matrix[i][0]:
                return False
            else :
                for j in range ( len ( matrix[0] ) ): 
                    if target == matrix[i][j]:
                        return True 
                    
# dealing with two lists with different size         
            
questions = ['name', 'quest', 'favorite color','asd']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))