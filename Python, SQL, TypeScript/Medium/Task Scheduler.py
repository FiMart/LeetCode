class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_count = max(task_count.values())
        max_count_tasks = sum(1 for count in task_count.values() if count == max_count)
        
        # Calculate the number of slots needed
        slots = (max_count - 1) * (n + 1) + max_count_tasks
        
        # The result is the maximum between the length of tasks and the calculated slots
        return max(len(tasks), slots)