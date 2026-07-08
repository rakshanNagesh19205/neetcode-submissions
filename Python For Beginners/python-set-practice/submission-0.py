from typing import List,Set

def contains_duplicate(words: List[str]) -> bool:
    result = False
    resultset = set()
    
    for word in words:

        if word not in resultset:
            resultset.add(word)
        else:
            result = True

    return result

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
