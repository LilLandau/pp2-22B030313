def permutation(word, buffer):
    if len(word) == 0:
        print(buffer, end=" ")
        return

    for i in range(len(word)):
        curr = word[i]              #выбирается символ
        left = word[0:i]            
        right = word[i+1:]
        substr = left + right        #вырез слова без символа

        permutation(substr, buffer + curr)      #рекурсия
