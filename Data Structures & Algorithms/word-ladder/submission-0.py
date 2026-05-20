
# Intuition
# Instead of precomputing the entire adjacency graph, 
# we can generate neighbors on the fly. 
# For each word, we try replacing each character with all 26 letters. 
# If the resulting word exists in our word set, it is a valid neighbor. 
# This approach trades precomputation time for potentially more 
# neighbor generation during BFS.

# Algorithm
# Convert the word list to a set for O(1) lookups.

# Start BFS from beginWord with distance counter set to 0.

# For each word in the current level, generate all possible words by 
# changing one character at a time.

# If a generated word is in the word set, 
# add it to the queue and remove it from the set to mark as visited.

# Return the distance when endWord is found, or 0 if the queue empties.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, res = set(wordList), 0

        q = deque([beginWord])

        while q:
            res += 1 # number of transformation sequences

            for _ in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return res

                for i in range(len(node)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        
                        if ch == node[i]: # unintentionally transform to the same work, ignore
                            continue
                        
                        nei = node[:i] + ch + node[i+1:] #start->i + new char + i+1->end
                        
                        # if this new word is in the list, 
                        # we add it to the queue for futrhter explorationa 
                        # and remove it from the set to prevent re-exploring it
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0
