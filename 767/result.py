import operator

class Solution(object):
    def reorganizeString(self, S):
        unique_char = list(set(S))
        double = self.make_adjacent(unique_char)
        char_occu = self.calc_char_occurence(S,unique_char)
        result = self.build_str(char_occu,unique_char,S)
        if len(result) != len(S): return ''
        for ea_double in double:
            adjacent = False
            if ea_double in result:
                adjacent = True
                return ''
        return result

    
    def build_str(self,char_occu,unique_char,S):
        string = [None] * len(S)
        prev_max_char = ''
        max_char = ''
        pointer = 0
        while True:
            max_val = max(char_occu.values())
            max_char = char_occu.keys()[char_occu.values().index(max_val)]
            for i in range(max_val):
               # print i,max_val,pointer,len(S)
                string[pointer] = max_char
                pointer = pointer + 2

                # reset pointer
                try:
                    if pointer > len(S)-1:
                        pointer = string.index(None)
                except ValueError:
                    pass 

            char_occu[max_char] = 0

            if not None in string: 
                break
        return ''.join(string) 

    def calc_char_occurence(self,S,unique_char):
        result = {}
        for ea_char in unique_char:
            result[ea_char] = S.count(ea_char)
        return result

    def make_adjacent(self,my_list):
        output = []
        for val in my_list:
            output.append(val*2)
        return output

            
#Solution().reorganizeString('aab')
Solution().reorganizeString('aaab')
Solution().reorganizeString('vvvlo')
Solution().reorganizeString('blflxll')
