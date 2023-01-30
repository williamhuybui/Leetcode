class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for i in range(len(points)):
            dist_list.append((points[i][0]**2 + points[i][1]**2, i))
        print(dist_list)
        dist_list.sort()
        ids = [k[1] for k in dist_list[:k]]
        return [points[id] for id in ids]
