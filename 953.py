class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_ = {order[i]: i for i in range(len(order))}
        res = []
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if dict_[w1[j]] > dict_[w2[j]]:
                    return False
                elif dict_[w1[j]] < dict_[w2[j]]:
                    break
                else:
                    if (j == min_len - 1) and (len(w1) > len(w2)):
                        return False
        return True
