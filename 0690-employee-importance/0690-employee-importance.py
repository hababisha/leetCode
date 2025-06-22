"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
  def getImportance(self, employees: list['Employee'], id: int) -> int:
    idToEmployee = {employee.id: employee for employee in employees}

    def dfs(id):
      values = idToEmployee[id].importance
      for subId in idToEmployee[id].subordinates:
        values += dfs(subId)
      return values

    return dfs(id)