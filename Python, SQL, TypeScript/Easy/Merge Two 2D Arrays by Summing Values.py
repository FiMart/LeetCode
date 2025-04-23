class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to store the sum of values for each unique index
        merged_dict = {}

        # Process the first array
        for index, value in nums1:
            if index in merged_dict:
                merged_dict[index] += value
            else:
                merged_dict[index] = value

        # Process the second array
        for index, value in nums2:
            if index in merged_dict:
                merged_dict[index] += value
            else:
                merged_dict[index] = value

        # Convert the dictionary back to a list of lists and sort by index
        merged_list = [[index, value] for index, value in merged_dict.items()]
        merged_list.sort(key=lambda x: x[0])

        return merged_list