class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_index = {int(num_str[i]): i for i in range(len(num_str))}
        for i in range(len(num_str)):
            for j in range(9, int(num_str[i]), -1):
                if j in max_index and max_index[j] > i:
                    num_str[i], num_str[max_index[j]] = num_str[max_index[j]], num_str[i]
                    return int(''.join(num_str))
        return num