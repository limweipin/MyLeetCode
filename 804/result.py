class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        #mc_dict =  dict(enumerate(mc))
        mc_dict = {}
        for k,v in enumerate(mc):
            mc_dict[chr(k+97)] = v

        result = set()
        for ea_word in words:
            mc_for_word = ''
            for i in range(len(ea_word)):
                mc_for_word = mc_for_word + mc_dict[ea_word[i]]
            result.add(mc_for_word)

        return len(result)

Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
