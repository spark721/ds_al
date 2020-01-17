from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        arr = [ amount + 1 for _ in range(amount + 1) ]
        arr[0] = 0
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (i == coins[j]):
                    arr[i] = 1
                    break
                elif (i > coins[j]):
                    prev = arr[i - coins[j]]
                    arr[i] = min(prev + 1, arr[i])

        return arr[amount] if arr[amount] < amount + 1 else -1


print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([186, 419, 83, 408], 6249))