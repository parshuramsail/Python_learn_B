#MASTER YODHA:given a sentence ,return a sentence  with a word reversed.
#master_yodha('i am home')===home am i
#master_yodha('where are you')====you are where
def master_yodha(name):
    master=name.split()
    return master[::-1]
print(master_yodha('my name is khan'))

#method1
def master_yodha(name):
    master=name.split()
    rever=master[::-1]
    return ' '.join(rever)
 print(master_yodha('my name is khan'))
