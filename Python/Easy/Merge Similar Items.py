class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1_dict = {item[0]: item[1] for item in items1}
        items2_dict = {item[0]: item[1] for item in items2}
        
        # Merge the two dictionaries
        merged_dict = {}
        for key in set(items1_dict.keys()).union(set(items2_dict.keys())):
            merged_dict[key] = items1_dict.get(key, 0) + items2_dict.get(key, 0)
        
        # Convert the merged dictionary back to a list of lists and sort by the first element
        merged_list = sorted(merged_dict.items())
        
        return merged_list  