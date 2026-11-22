class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(n, s, i):
            if s == target and n not in res:
                res.append(n.copy())
                return

            if i >= len(candidates) or s > target:
                return

            n.append(candidates[i])
            backtrack(n, s + candidates[i], i + 1)
            n.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(n, s, i + 1)
        
        backtrack([], 0, 0)
        return res


            


        