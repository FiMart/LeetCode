class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the people by height in descending order and by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue