def count_words(letters_list, vowels_set, target_length=3):
    stack = [([], 0)]
    total_words = 0
    total_backtracks = 0

    while stack:
        current_word, _ = stack.pop()

        if len(current_word) == target_length:
            total_words += 1
            total_backtracks += 1
            continue

        for letter in letters_list:
            if current_word and current_word[-1] in vowels_set and letter in vowels_set:
                continue
            stack.append((current_word + [letter], 0))
            total_backtracks += 1

    return total_words, total_backtracks


chosen_letters = ['A', 'E', 'B', 'C', 'I']
chosen_vowels = {'A', 'E', 'I'}

words_count, backtrack_count = count_words(chosen_letters, chosen_vowels, target_length=3)
print("Liczba słów:", words_count)
print("Liczba cofnięć:", backtrack_count)
