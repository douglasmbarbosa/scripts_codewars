'''
Escreva uma função que receba uma string de uma ou mais palavras
e retorne a mesma string, mas com todas as palavras de cinco ou 
mais letras invertidas (exatamente como o nome deste Kata). 
As strings passadas consistirão apenas em letras e espaços. 
Espaços serão incluídos somente quando houver mais de uma palavra.

'''

def spin_words(sentenca):
    # Your code goes here
    posicao_palavras = []
    posicao_palavras.append(0)
    posicao = 1
    nova_sentenca = ''
    n = len(sentenca)
    numero_de_palavras = 0
    for i in range(len(sentenca)):
        if sentenca[i] == ' ':
            if i - posicao > 4:
                nova_sentenca += sentenca[-(n - i - 1):-(n ):-1]
             
    for j in range (len(posicao_palavras)):
        if posicao_palavras[j+1] - posicao_palavras [j] - 1 > 4:
            f
    print(posicao_palavras)
    # numero_de_palavras +=1
    # print(numero_de_palavras)
    # palavras = [numero_de_palavras]
    # for i in range(len(sentenca)):
    #     #print(sentenca[i])
    #     if sentenca[i] != ' ':
    #         str(palavras[posicao_palavras]) += sentenca[i]
    #     else:
    #         posicao_palavras += 1
        # if sentenca[i] == ' '
        #     numero_de_palavras += 1
        #     tamanho_das_palavras = 
        
    
    #return resultado
    #return palavras
    return posicao_palavras
    
    #  - 10987654321 
frase = 'Hey fellow '
resultado = spin_words(frase)
print(resultado)