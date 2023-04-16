sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)
    
print(solution(sentence1))
print(solution(sentence2))


def solution_2(sentence):
    chars_to_remove = "!?',;."
    for i in chars_to_remove:
        sentence = sentence.replace(i, '')

    words = sentence.split()
    len_of_words = len(words)

    return round(sum(len(word) for word in words) / len_of_words, 2)


print(solution_2(sentence1))
print(solution_2(sentence2))
