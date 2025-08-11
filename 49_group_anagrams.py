

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # Loop through words and sort to get 'unique' anagram
    # If not seen before, add as key to hashmap
    # If seen before, then append to list for key
    
    res = dict()
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in res.keys():
            res[sorted_word] = [word]
        else:
            res[sorted_word].append(word)
    return list(res.values())


tt = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(tt))