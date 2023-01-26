'''
Escreva uma função que receba uma string de uma ou mais palavras
e retorne a mesma string, mas com todas as palavras de cinco ou 
mais letras invertidas (exatamente como o nome deste Kata). 
As strings passadas consistirão apenas em letras e espaços. 
Espaços serão incluídos somente quando houver mais de uma palavra.

'''

def spin_words(sentence):
    # Your code goes here
    posicao_palavras = 0 
    numero_de_palavras = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
             numero_de_palavras += 1
    numero_de_palavras +=1
    print(numero_de_palavras)
    palavras = [numero_de_palavras]
    for i in range(len(sentence)):
        #print(sentence[i])
        if sentence[i] != ' ':
            str(palavras[posicao_palavras]) += sentence[i]
        else:
            posicao_palavras += 1
        # if sentence[i] == ' '
        #     numero_de_palavras += 1
        #     tamanho_das_palavras = 
        
    
    #return resultado
    return palavras
    
    
frase = 'Hey fellow warriors'
resultado = spin_words(frase)
print(resultado)