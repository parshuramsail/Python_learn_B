#ENUMERATE
#BEFOR USING ENUMERATE
#index_count=0
#for letter in 'abcde':
#    print("at index {} the letter is :{} ".format(index_count,letter))
#    index_count+=1

#BEFORE USING ENUMERATE
#index_count=0
#word='abcdeffght'
#for letter in word:
#    print(word[index_count])
#    index_count+=1

#AFTER USING ENUMERATE
#word='ABCDEFGHIJK'
#for index,letter in enumerate(word):
#    print('at index {} the letter is:{}'.format(index,letter))

word='ABCDEFGHIJK'
for index,letter in enumerate(word):
    print(index,letter)
