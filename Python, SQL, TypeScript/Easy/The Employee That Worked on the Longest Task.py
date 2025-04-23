class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = 0
        max_id = 0
        prev_time = 0

        for log in logs:
            id, time = log
            time_spent = time - prev_time
            if time_spent > max_time or (time_spent == max_time and id < max_id):
                max_time = time_spent
                max_id = id
            prev_time = time

        return max_id