def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)

words = input("Enter words separated by spaces: ").split()

word, length = longest_word(words)

print("Longest word:", word)
print("Length:", length)
