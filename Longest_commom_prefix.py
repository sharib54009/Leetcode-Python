# LeetCode: Longest commom prefix
# Difficulty: Easy
# Focus: Python basics, loops, conditional statements
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in strs:
            if i >= len(j) or j[i] != char:
                return prefix
        prefix += char
    return prefix
strs = ["heat", "height", "helicopter"]
print("longest commom prefix is : ", longest_common_prefix(strs)) 