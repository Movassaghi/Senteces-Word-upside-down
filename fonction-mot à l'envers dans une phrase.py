## BUT: Creer une fonction qui fait les mot de la phrase à l'envers mais sur sa place

def Word_invers(phrase):

    sen = phrase.split() 
    print(sen)
    
    new_sen = [] 
    
    for elm in sen:
        word = list(elm)

        invers_word = []
        for i in range(0, len(word)):
            invers_word.append(word[(-i+len(word))-1])
            i +=i
        invers_word = "".join(invers_word)
        new_sen.append(invers_word)
        elm +=elm

     
    print(new_sen)
    invers_sen = ' '.join(new_sen)
    print(invers_sen)

    
text = input("entrez une phrase:")
Word_invers(text)    
        
