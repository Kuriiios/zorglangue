def zorglangue_translator(texte):
    splitted_text = texte.split(' ')
    reversed_splited_list = []
    for word in splitted_text:
        word_str = ''.join(list(word)[::-1])
        reversed_splited_list.append(word_str)
   
    reversed_text = ' '.join(reversed_splited_list)
    return reversed_text