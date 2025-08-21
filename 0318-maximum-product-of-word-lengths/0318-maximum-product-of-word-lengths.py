class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        n = len(words)
        # Store bitmask representation of each word
        bitmasks = [0] * n  
        lengths = [len(word) for word in words]

        # Convert words into bitmasks
        for i in range(n):
            for char in words[i]:
                bitmasks[i] |= (1 << (ord(char) - ord('a')))
        
        max_len = 0
        # Compare each word with brute force
        for i in range(n-1):
            for j in range(i+1, n):
                # check if they don't share any common word
                if bitmasks[i] & bitmasks[j] == 0:
                    max_len = max(max_len, lengths[i]*lengths[j])
    

        return max_len

        