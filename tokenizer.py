def tokenize(text):
    words = text.lower().split()
    counts = {}
    for word in words:
         if word in counts:
             counts[word]+= 1
         else:
             counts[word]=1
    return counts
print(tokenize("create the things you wish existed"))
print(tokenize("forreve prints forreve"))
