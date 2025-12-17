# Two Sum Algorithm

## problem
Het input is een lijst ben gehele getallen `num` en een doelgetal `target`, vind de indices van de **twee getallen** die sammen `target` vormen dus het zelfde waarde. Elke element kan slechts een keer gebruik worden en het rezultaat met een lijst zijn `[index1, index2]`

## Constraints

- `2 <= len(nums) <= 10^4`  
  Deze betekent dat de lijst **minimaal 2 elementen** moet hebben en **maximaal 10.000 elementen**.

- `-10^9 <= nums[i] <= 10^9`  
  Dit betekent dat elk element in de lijst tussen **-1.000.000.000** en **1.000.000.000** kan liggen.

- `-10^9 <= target <= 10^9`  
  Dit geeft aan dat het doelgetal `target` minimaal **-1.000.000.000** en maximaal **1.000.000.000** kan zijn.

---

## Oplossing in Python

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Validatie van constraints
        assert -10**9 <= target <= 10**9
        assert 2 <= len(nums) <= 10**4
        for x in nums:
            assert -10**9 <= x <= 10**9

        # Gebruik een hashmap (dictionary) voor snelle lookup
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

```
