word=input("enter a word:")
vowels=[]
for ch in word:
 if ch.lower() in "aeiou":
  vowels.append(ch)
print("list the vowels:",vowels)
