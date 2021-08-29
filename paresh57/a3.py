#OLD MACDONALD:write a function that capitalize the first and fourth letter of name.
#macdonald===MacDonald
def old_macdonald(name):
    first=name[0]
    second=name[1:3]
    three=name[3]
    four=name[4:]

    return first.upper()+second+three.upper()+four
print(old_macdonald('macdonald'))

#CAPITALIIZE METHOD
def old_macdonald(name):
    first=name[:3]
    second=name[3:]

    return first.capitalize()+second.capitalize()
print(old_macdonald('macdonald'))
