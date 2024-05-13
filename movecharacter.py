#EXMPLE-1
def move_char_to_end(word, ch):
    index = word.index(ch)
    reversed_substring = word[:index+1][::-1]
    final_word = reversed_substring + word[index+1:].replace(ch,'')
    return final_word



#EXAMPLE-2
def move_character(word,ch):
    index = word.find(ch)
    if index != -1:
        new_word = ch + word[:index] + word[index+1:]
        return new_word
    else:
        return word



def remove_character(word, ch):
    if ch not in word:
        return word
    else:
        return word.replace(ch, "")
