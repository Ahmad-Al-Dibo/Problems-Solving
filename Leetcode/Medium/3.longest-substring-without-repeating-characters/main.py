

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """
      Taking time: 37 ms
      Beats: 16.28%
      Analyze Complexity
      Memory
      49.21 MB
      Beats: 8.68%
      """
        if not s:
            return 0

        new_tekens = []  # lijst van unieke substrings
        huidig_list = []  # de huidige substring

        for teken in s:
            if teken in huidig_list:
                # Voeg de huidige substring toe en begin een nieuwe vanaf de herhaling
                new_tekens.append(huidig_list)
                # Start een nieuwe substring vanaf het teken ná de eerste herhaling
                idx = huidig_list.index(teken)
                huidig_list = huidig_list[idx + 1:]
            
            huidig_list.append(teken)

        # Voeg de laatste substring toe
        new_tekens.append(huidig_list)

        # Vind de langste substring
        max_len = max(len(sub) for sub in new_tekens)
        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """ 
      Runtime: 18 ms
      Beats: 57.74%
      
      Memory: 19.36 MB
      Beats: 8.68%
      """
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
