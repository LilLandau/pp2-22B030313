def reverse(sentences):
    if len(sentences) == 0:
        return
    
    words = sentences.split()               #разбиваю предложение на слова
    for i in range(len(words)-1, -1, -1):   #пробегаюсь по циклу с конца
        print(words[i])

    return