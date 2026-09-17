class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Store vowels in a set for O(1) lookups
        vowels = set("aeiou")

        # prefix_count[i] = number of qualifying words in words[0:i]
        # Index 0 is 0 because there are no words before index 0
        prefix_count = [0] * (len(words) + 1)

        # Running count of valid words seen so far
        preSum = 0

        # Build prefix counts
        for i, w in enumerate(words):
            # Check if current word starts and ends with a vowel
            if w[0] in vowels and w[-1] in vowels:
                preSum += 1

            # Store the count of valid words up to and including index i
            prefix_count[i + 1] = preSum

        # Result array for all queries
        res = [0] * len(queries)

        # Answer each range query using prefix sums
        for i, q in enumerate(queries):
            l, r = q

            # Count valid words from index l to r inclusive:
            # valid words up to r minus valid words before l
            res[i] = prefix_count[r + 1] - prefix_count[l]

        return res