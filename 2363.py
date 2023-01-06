class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = {}
        for item in items1 + items2:
            if item[0] not in ret:
                ret[item[0]] = item[1]
            else:
                ret[item[0]] += item[1]
        return sorted(list(ret.items()))
