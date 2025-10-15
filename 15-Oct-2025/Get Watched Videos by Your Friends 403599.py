# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

from collections import defaultdict, deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs = deque()
        levels = [-1]*len(watchedVideos)
        levels[id] = 0
        bfs.appendleft(id)
        d = defaultdict(int)
        while len(bfs):
            a = bfs[-1]
            bfs.pop()
            if levels[a] == level:
                for x in watchedVideos[a]:
                    d[x] += 1

            for f in friends[a]:
                if levels[f] == -1:
                    levels[f] = levels[a] + 1
                    bfs.appendleft(f)

        return sorted([x for x in d], key = lambda x : (d[x], x))