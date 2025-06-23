# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = [0]*2001
        for e in employees:
            emp[e.id] = e

        stack = [emp[id]]
        total = 0
        while len(stack):
            s = stack[-1]
            stack.pop()
            total += s.importance
            for x in s.subordinates:
                stack.append(emp[x])
        return total