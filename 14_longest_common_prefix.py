"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""



def longestCommonPrefix(strs: list[str]) -> str:
    # loop through longest word, letter by letter
    # check if all words starts with current prefix
    
    longest_word = max(strs, key=len)
    longest_prefix = ''
    prefix = ''
    for letter in list(longest_word):
        prefix += letter
        if all([s.startswith(prefix) for s in strs]):
            longest_prefix = prefix
        
    return longest_prefix


print(longestCommonPrefix(["flower","flow","flight"]))
