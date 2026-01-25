class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        charindex = 0
        characters = list(s)
        sequence = []

        for i in list(t):
            if i in characters:
                if i == characters[charindex]:
                    sequence.append(i)
                    if not charindex-1 > len(characters):
                        charindex+=1
        # print("INPUT: ", list(t))
        # print("OUTPUT: ", sequence)        
        return True if characters == sequence else False
