class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_formula = lambda p: p[0]**2 + p[1]**2
        
        def partition(left, right):
            pivot_dist = dist_formula(points[right])

            for i in range(left, right):
                i_dist = dist_formula(points[i])

                if i_dist < pivot_dist:
                    points[i], points[left] = points[left], points[i]
                    left += 1

            points[left], points[right] = points[right], points[left]
            return left
        
        left = 0
        right = len(points) - 1
        pivot_index = len(points)

        while pivot_index != k:
            pivot_index = partition(left, right)
            if pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
        
        return points[:k]

