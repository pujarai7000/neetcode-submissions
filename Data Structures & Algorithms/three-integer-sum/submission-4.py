
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # Sort the array
        result = []  # Store unique triplets

        # -2 ensures we leave at least two positions after i
        for i in range(len(nums) - 2):

            # Avoid generating duplicate combinations
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # i > 0:
            # Makes sure checking the previous starting number
            # is appropriate.

            # nums[i] == nums[i - 1]:
            # Detects a repeated starting number.

            # continue:
            # Skips that starting number to avoid duplicate triplets.

            left = i + 1  # Start immediately after i
            right = len(nums) - 1  # Start at the last index

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found three numbers adding up to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    # Prevents adding the same triplet again
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total > 0:
                    # Sum is too large, move right backward
                    right -= 1

                else:
                    # Sum is too small, move left forward
                    left += 1

        # Return only after checking all possible triplets
        return result

  
 