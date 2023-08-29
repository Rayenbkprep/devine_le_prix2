import random

# tirage au sort d'un prix
# choix du prix du joueur
# message 'Bravo' si le prix est trouvé
# mssage 'Pas assez' si le pris est trop bas
# Message 'trop elevé' si le prix est trop haut
# message 'perdu' au bout de 5 essais
# fin au bout de 5 essais ou si le prix a été trouvé

prix = random.randint(0, 4)
    for i in range(5):
        essai = int(input('Quel est le prix : '))

        if prix > essai:
            print('Pas assez')
        elif prix < essai:
            print('trop élevé')
        else:
            print('Bravo, vous avez trouvé le bon prix!')
            break
    else:
        print('Perdu, vous n avez pas trouvé le bon prix. Le prix était', prix)


