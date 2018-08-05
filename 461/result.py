class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_x = format(x, "032b")
        binary_y = format(y, "032b")
        print binary_x,binary_y
        count = 0
        for idx,val in enumerate(binary_x):
            if binary_y[idx] != binary_x[idx]:
                count += 1
        return count

Solution().hammingDistance(1,4)
