import random
from hangman import dibujo
n = random.randint(0, 849)
dick=open('diccionario.txt')
d=[]
cheat=[]
for l in dick:
    d.append(l.strip())
word=d[n]
result=('-'*(len(word)))
print(result)
estado=list('-'*(len(word)))
result=''
score=7
cont=0
guesses=[]
jugar='y'
while jugar=='y':
    over=False
    print(result)
    guess = input('adivina:')
    guesses.append(guess)
    if guess in word:
        print('yep')
        cont=0
        for i in word:
            if i==guess:
                estado[cont]=i
            cont+=1

    else:
        print('nop')
        score-=1
    result=''.join(estado)
    print('palabras usadas:', guesses)
    print(result)
    for l in dibujo(score):
        print(l)

    if result==word:
        n = random.randint(0, 849)
        print('u win')
        jugar=input('d nuevo? [y/n]')
        over=True

    if score==1:
        n = random.randint(0, 849)
        print('u lose, era', word)
        jugar =input('d nuevo? [y/n]')
        over=True
    if over:
        word = d[n]
        result = ('-' * (len(word)))
        estado = list('-' * (len(word)))
        result = ('-' * (len(word)))
        score = 7
        cont = 0
        guesses = []



print('-------------------------')