sentenca = 'prim testando '
n = len(sentenca)
nova_sentenca = ''
pos = 0
for i in range(n):
    if sentenca[i] == ' ':
        if i - pos > 4:
            nova_sentenca += sentenca[-(n - i + 1):-(n - pos + 1):-1]

        
        #else:

            #nova_sentenca += ...
        pos = i + 1
        nova_sentenca += ' '
print(nova_sentenca)