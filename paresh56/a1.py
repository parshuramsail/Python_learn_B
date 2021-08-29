#pig latin
#if word starts with vowel,add ay to end.
#if word does not start with vowel then add first letter at the end .then add ay
#word===wordway
#apple==appleay

def pig_latin(word):
    first_leter=word[0]

    if first_leter in 'aeiou':
            pig_word=word +'ay'
    else:
        pig_word=word[1:]+first_leter +'ay'
    return pig_word
c=pig_latin("word")
print(c)
