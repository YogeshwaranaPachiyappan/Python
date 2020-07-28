def makeAnagram(a, b): 
    buffer = [0] * 26
    for char in a: 
        buffer[ord(char) - ord('a')] += 1
    for char in b: 
        buffer[ord(char) - ord('a')] -= 1
    return sum(map(abs, buffer)) 
str1 = input()
str2 = input()
print(makeAnagram(str1, str2)) 
