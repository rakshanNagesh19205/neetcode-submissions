from typing import List

def count_unique_words(words: List[str]) -> int:
    result = 0
    resultset = set()
    for word in words:
        resultset.add(word)

    result = len(resultset)
    return result
    

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
