class Solution:
    def encode(self, strs):
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':          # go to #
                j += 1
            length = int(s[i:j])        # get number before #

            word = s[j+1 : j+1+length]  # skip #, grab chars for word
            result.append(word)

            i = j + 1 + length          # jump to next chunk
        return result


