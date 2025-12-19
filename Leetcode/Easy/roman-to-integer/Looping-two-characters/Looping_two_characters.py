# Looping two characters at a time.



class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ru = 0
        
        for a, b in zip(s, s[:1]):
            if roman[a] < roman[b]:
                ru -= roman[a]
            else:
                ru += roman[a]
        return ru + roman[s[-1]]
        


su = Solution().romanToInt("II")  # [1, 1]
print(su) 
