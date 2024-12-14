import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = np.array(nums)
        idx_list = []
        last_idx = None
        while target > 0:
            closest_idx = (np.abs(target - array)).argmin()
            if not last_idx == closest_idx:
                target = target - array[closest_idx]
                last_idx = closest_idx
                idx_list.append(closest_idx)
            else:
                np.delete(array,closest_idx) 
                closest_idx = (np.abs(target - array)).argmin() +  1
                target = target - array[closest_idx]
                idx_list.append(closest_idx)
        return idx_list
        
