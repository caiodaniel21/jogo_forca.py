from random import choice

palavras = ['computador', 'tela', 'fábrica', 'luz', 'física', 'teclas', 'sexo', 'ventilador', 'mochila', 'janela']

palavra = choice(palavras)

digitadas = []
acertos = []
erros = 0

while True:
    senha_string = ''
    senha = ''
    for letra in palavra:
        senha_string += f'{letra} ' if letra in acertos else '_ '
        senha += letra if letra in acertos else '_'
    print (senha_string)
    if senha == palavra:
        print ('Parabéns, você acertou!')
        break
    tentativa = input('Digite uma letra como tentativa: ')
    if tentativa == palavra:
        print ('Parabéns, você acertou!')
        break
    if tentativa in digitadas:
        print ('Você já digitou essa letra, tente outra novamente!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print ('Você errou!')
    
    print ('X===:')
    print ('X   O' if erros >= 1 else 'X')

    linha2 = ''
    if erros == 2:
        linha2 += 'X   |'
    elif erros == 3:
        linha2 += 'X  /|'
    elif erros >= 4:
        linha2 += 'X  /|\ '
    
    print (linha2)

    linha3 = ''
    if erros == 5:
        linha3 += 'X  /'
    elif erros >= 6:
        linha3 += 'X  / \ '
    
    print (linha3)

    if erros >= 6:
        print (f'Você foi enforcado, a palavra era: {palavra}')
        break
