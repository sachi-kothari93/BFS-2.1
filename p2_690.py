# 690. Employee Importance

# TC : O(n) where n is the total number of employees in the organization
    # Each employee is processed exactly once through the recursive calls
    # The dictionary creation is also O(n)

# SC : O(n) for the employee dictionary that maps IDs to employee objects
    # O(h) additional space for the recursion stack, where h is the height of the employee hierarchy
    # In the worst case (completely linear hierarchy), h could be n, making worst-case space complexity O(n)

# Did this code successfully run on Leetcode : yes

# Approach :
# We define the getImportance method taking the employee list and target ID as parameters
# We create a dictionary mapping employee IDs to their objects for O(1) lookups
# We define a helper function calculate_importance that computes total importance recursively
# For each employee, we start with their own importance value
# Then, we recursively add the importance of each subordinate
# This recursion automatically handles both direct and indirect subordinates
# Then start the calculation with our target employee ID and return the result

# This solution uses depth-first search (DFS) to traverse the employee hierarchy and calculate the total importance value.

from typing import List, Optional

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create a dictionary for quick employee lookup by ID
        emp_dict = {employee.id: employee for employee in employees}
        
        # Define a recursive helper function to calculate total importance
        def calculate_importance(emp_id):
            # Get the employee object
            employee = emp_dict[emp_id]
            
            # Start with the employee's own importance
            total = employee.importance
            
            # Add importance of all subordinates recursively
            for subordinate_id in employee.subordinates:
                total += calculate_importance(subordinate_id)
                
            return total
        
        # Start the calculation from the given employee ID
        return calculate_importance(id)
            