def Word_invers(phrase):

    # entrez une phrase
    #phrase = input("entrer une phrase:")
    sen = phrase.split() # mettre une phrase dans une liste comme phrase
    print(sen)
    #print(len(sen))

    ## But: le but de garder chaque mot sur sa place et juste l'avoir à l'envers
    
    new_sen = [] #crée une liste vide pour mettre chaque element inversé de la phrase dans une autre liste

    # mettre chaque element de la liste "sen", dans une liste "word"
    for elm in sen:
        word = list(elm)
    ##    print(word)
    ##    print(len(word))

    
    # BUT : chaque mot qui est dans une liste soit à l'envers    
    # les element de la liste de invers_word commence par la dernier element
    # de la liste de word_list jusqu'au debut. la fin vers le debut 
    # on crée une liste vide pour chaque mot
        
        invers_word = []
        for i in range(0, len(word)):
            #print(word[(-i+len(word))-1])
            invers_word.append(word[(-i+len(word))-1])
            i +=i
        
        invers_word = "".join(invers_word) # on attache les lettre pour avoir un mot inversé et on l'ajoute à la liste new_sen
        new_sen.append(invers_word)
        elm +=elm

     
    print(new_sen)

    # afficher la nouvelle phrase avec des mot à l'envers
    # on attache les elements de la liste avec la fonction join et la separation espace
    
    invers_sen = ' '.join(new_sen)
    print(invers_sen)

    
text = input("entrer une phrase:")
Word_invers(text)    
        
