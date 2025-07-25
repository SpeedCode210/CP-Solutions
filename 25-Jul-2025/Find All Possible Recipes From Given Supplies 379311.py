# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        D = defaultdict(lambda : [])
        Degs = defaultdict(int)
        for i in range(len(recipes)):
            for x in ingredients[i]:
                Degs[recipes[i]] += 1
                D[x].append(recipes[i])

        print(D)
        bfs = deque()
        for x in recipes:
            if Degs[x] == 0:
                bfs.append(x)

        for x in supplies:
            if Degs[x] == 0:
                bfs.append(x)

        topo = []
        while len(bfs):
            x = bfs[0]
            bfs.popleft()
            topo.append(x)
            for y in D[x]:
                Degs[y] -= 1
                if Degs[y] == 0:
                    bfs.append(y)

        return [x for x in topo if x in recipes]