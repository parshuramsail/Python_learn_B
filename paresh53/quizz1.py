st='S print the only words that starts wih s in this statement'
for word in st.split():
    if word[0].lower=='S':
        print(word)
