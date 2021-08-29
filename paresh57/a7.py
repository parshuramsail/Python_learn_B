#PAPER DOLL:given string,return string where for every character in the original there are the tree characters.
#paper_doll('hello')==hhheeellllllooo)
#paper_doll(mississippi)==mmmiiisssiiissssssiiippppppiii
def paper_doll(text):
    result=''
    for char in text:
        result+=char*3
    return result
print(paper_doll("miss"))
