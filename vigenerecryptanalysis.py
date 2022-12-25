import detectEnglish,vigenereCipher

def hackVigenere(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    possible_decodes=[]
    best_sol=''
    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word,ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            possible_decodes.append('Key ' + str(word) + ': ' + '\t' +decryptedText[:100])
    for choice in possible_decodes:
        if detectEnglish.isEnglish(choice, wordPercentage=80):
            best_sol=choice
            break
    return possible_decodes,best_sol

