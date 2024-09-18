class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split()
        words_s2 = s2.split()
        all_words = words_s1 + words_s2

        word_count = Counter(all_words)

        uncommonArray = [key for  key , val in word_count.items() if val ==1]
        return uncommonArray
