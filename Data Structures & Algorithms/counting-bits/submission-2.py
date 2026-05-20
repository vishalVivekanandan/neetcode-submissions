class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            numOfOnes = bin(i).count('1')
            output.append(numOfOnes)
        return output
        