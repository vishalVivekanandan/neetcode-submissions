class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain a sliding window where you start l and r as 0
        # while r <= len(s) - 1
        # expand r until you have one of each t char (use hashmap to keep track)
            # use temp var to track this and re-assign it to count = min(count, temp)
        # if you do, then move left until you dont have at least one of t
        # then repeat step with r
            # re-assign count to min of new value, and count

        # now move l until you dont have 1 of t

        # return count if count != inf else return ""
 
        if not s or not t or len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # Current counts inside the sliding window
        window = {}

        # Number of distinct characters whose required frequency is satisfied
        formed = 0
        required = len(need)

        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]

            # Add current right character into the window
            window[char] = window.get(char, 0) + 1

            # If this character is needed and we now have enough of it,
            # mark one requirement as satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Try shrinking from the left while the window is valid
            while formed == required:
                window_len = right - left + 1

                # Update best answer if this window is smaller
                if window_len < best_len:
                    best_len = window_len
                    best_start = left
                
                # remove leftmost character from window
                left_char = s[left]
                window[left_char] -= 1

                # window is no longer valid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]
            

