class solution(self,):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

a = (('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))
for item in a:
    print(item[1])

b = "hello world"
b = b.replace(" ", "")  # Changed: use replace() instead of strip()
print(tuple(b))  # Now prints: ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
print(list(b))   # Now prints: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

obj = solution()
y = obj.twoSum([2,7,11,15], 9)
print(y)