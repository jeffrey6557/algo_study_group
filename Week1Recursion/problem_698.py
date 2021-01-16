class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # base case
        if len(nums) < k:
            return False
        total = sum(nums)
        if total % k:
            return False

        target = total / k 


        seen = [False] * len(nums)
        def checkPartitions(offset, k, partial_sum, seen):
            
            # base case: one subset left means success
            if k == 1:
                return True

            # general case: assume we solved problem of size k-1
            # i.e. given the offset of the number we are considering, 
            # the partial sum we are adding to, and numbers we have seen, 
            # we need to assemble the answer to the problem of size k

            # if we have found a subset, reduce to the problem of size k-1 
            # and zero out partial_sum and offset
            if partial_sum == target:
                return checkPartitions(0, k-1, 0, seen)

            # otherwise, add numbers iteratively to partial sums if possible
            for i in range(offset, len(nums)):
                if not seen[i] and partial_sum + nums[i] <= target:
                    seen[i] = True 
                    # if we can solve the remaining problem for the next position, 
                    # we are done
                    if checkPartitions(offset+1, k, partial_sum+nums[i], seen):
                        return True
                    # otherwise, mark not seen for the position
                    seen[i] = False
            # after exhausting all the numbers, we have not solved the problem
            return False
        
        # simplify the problem if we have qualified singleton
        nums.sort()
        if nums[-1] > target: 
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return checkPartitions(0, k, 0, seen)