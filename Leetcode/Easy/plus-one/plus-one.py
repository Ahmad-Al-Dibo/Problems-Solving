class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ""
        for i in digits:
            digits_str += str(i)
        number = int(digits_str) + 1
        return list(map(int, str(number)))
