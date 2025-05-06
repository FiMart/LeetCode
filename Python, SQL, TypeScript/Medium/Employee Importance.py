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
        employee_map = {employee.id: employee for employee in employees}
        total_importance = 0
        queue = [id]

        while queue:
            current_id = queue.pop(0)
            current_employee = employee_map[current_id]
            total_importance += current_employee.importance
            queue.extend(current_employee.subordinates)

        return total_importance