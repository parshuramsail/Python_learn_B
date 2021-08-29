#ANIMAL CRACKERS:write function takes a two word string and returns true if both words begins with same letter
#animal crackers('levelhead llama')===TRUE
#animal crackers('crazy kangaroo')===FALSE
#def animal_crackers(text):
#    word_list=text.split()
#    first=word_list[0]
#    second=word_list[1]
#    return first[0]==second[1]
#print(animal_crackers('levelhead llama'))
#print(animal_crackers('crazy kangaroo'))


def animal_crackers(text):
    word_list=text.split()
    return word_list[0][0]==word_list[1][0]
print(animal_crackers('levelhead llama'))
print(animal_crackers('crazy kangaroo'))



