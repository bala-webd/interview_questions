def remove_palindrome(sentence=None):
    if sentence and isinstance(sentence, str):
        words = sentence.split(' ')
        corrected_sentence = ""
        count = 0
        for word in words:
            is_palindrome = check_palindrome(word)
            if not is_palindrome:
                if count > 0:
                    word = f" {word}"
                corrected_sentence += word
                count += 1
        return corrected_sentence
    else:
        return "No Valid string provided"

def check_palindrome(word):
    reversed_word = ""
    for char_ind in range(len(word)):
        target_index = len(word) - 1
        reversed_word += word[target_index - char_ind]
    return word.lower() == reversed_word.lower()

sentence = 'Malayalam is my mother tongue'
print(remove_palindrome(sentence))
