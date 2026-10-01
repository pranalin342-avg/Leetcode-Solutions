class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0

        for customer in accounts:
            total = sum(customer)

            if total > ans:
                ans = total
        return ans
        