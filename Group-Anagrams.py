class Solution:
    #create a hashmap with key as a word, and value as the anagram
    #iterating through strs, if word is in anagram, append to the value array 
    #if not, create a value array with word in it
    #for example{\eat\: [\eat\, \tea\, \ate\], \bat\:[bat], \nat\: [\nat\, \tan\]}}
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams: anagrams[sorted_word].append(word)
            else: anagrams[sorted_word] = [word]
        return list(anagrams.values())