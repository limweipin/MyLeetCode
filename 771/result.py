class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        S = list(S)
        J = list(J) 
        result = 0
        for ea_j in J:
            result = result + S.count(ea_j)
        return result
Solution().numJewelsInStones('ab','SSSSA')
