from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for courseNumber, pre in prerequisites:
            prereq[courseNumber].append(pre)

        courseOrderToTake = []
        preFulfilled, pendingVerify = set(), set()

        def dfs(courseNumber):
            if courseNumber in pendingVerify:
                return False
            if courseNumber in preFulfilled:
                return True

            pendingVerify.add(courseNumber)
            for pre in prereq[courseNumber]:
                if dfs(pre) == False:
                    return False
            pendingVerify.remove(courseNumber)
            preFulfilled.add(courseNumber)
            courseOrderToTake.append(courseNumber)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return courseOrderToTake
#####################
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
############################## L
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = {}

        for des, src in prerequisites:
            adj_list[src].append(des)
            indegree[des] = indegree.get(des, 0) + 1

        no_src_course = deque([k for k in range(numCourses) if k not in indegree])
        course_seq = []

        while no_src_course:
            src = no_src_course.popleft()
            course_seq.append(src)

            for des in adj_list[src]:
                indegree[des] = indegree.get(des) - 1
                if indegree[des] == 0:
                    no_src_course.append(des)

        return course_seq if len(course_seq) == numCourses else []


"""
210. Course Schedule II
Medium

7859

266

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
Accepted
712,213
Submissions
1,493,650
"""