class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        required = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        return min(char_count[char] // required[char] for char in required)