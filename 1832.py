from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a_dict = Counter("abcdefghijklmnopqrstuvwxyz")
        a_dict.subtract(Counter(sentence))
        for key in a_dict:
            if a_dict[key] == 1:
                return False
        return True
            
