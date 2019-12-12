# © N.V.Proskuryakov 2019


# Промахи - отсутствие слова в массиве

def WordsComparison(coincidences, comparisonwords, words):
    for word in words:
        word_finded = False
        for word2 in comparisonwords:
            if (word == word2):
                word_finded = True
                coincidences.append(True)
                break
        if (word_finded == False):
            coincidences.append(False)

def CountTrueFalse(coincidences):
    true_count = 0
    false_count = 0
    for i in range(len(coincidences)):
        if (coincidences[i] == True):
            true_count += 1 # Добавить совпадение
        else:
            false_count += 1 # Добавить промах
    return false_count, true_count



def TwoStringsSplit(original_string, string_for_comparison):
    words = original_string.split(" ")
    comparisonwords = string_for_comparison.split(" ")
    return comparisonwords, words

def Comparison(original_string, string_for_comparison): # Сравнить строки на совпадения слов
    comparisonwords, words = TwoStringsSplit(original_string, string_for_comparison)
    coincidences = []
    WordsComparison(coincidences, comparisonwords, words)
    false_count, true_count = CountTrueFalse(coincidences)
    if (true_count > false_count):
        return True
    else:
        return False

def ComparisonCount(originalString, stringForComparison): # Вернуть количество совпадений и промахов
    comparisonwords, words = TwoStringsSplit(original_string, string_for_comparison)
    coincidences = []
    WordsComparison(coincidences, comparisonwords, words)
    false_count, true_count = CountTrueFalse(coincidences)
    Result = [true_count, false_count]
    return Result

def Missings(originalString, stringForComparison): # Вернуть слова, совпадения с которыми не нашлось
    comparisonwords, words = TwoStringsSplit(original_string, string_for_comparison)
    missings = []
    for word in words:
        word_finded = False
        for word2 in comparisonwords:
            if (word == word2):
                word_finded = True
                break
        if (word_finded == False):
            missings.append(word)
    return missings
