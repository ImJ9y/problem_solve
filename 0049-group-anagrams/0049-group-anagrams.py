class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_bank = defaultdict(list)


        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            
            word_bank[tuple(count)].append(word)
        
        return list(word_bank.values())
