import random

answer = random.randint(1,100)
i = 10

while i != 0:

    try:
        guess = int(input("Deviner le nombre : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if guess > answer :
        print(f"\nTrop haut")
        i = i - 1
    elif guess < answer:
        print(f"\nTrop bas")
        i = i - 1
    else : 
        break
    print(f"Il vous reste {i} essaies")

if guess == answer:
    print(f"\nVous avez trouvé !\nLa réponse était : {answer}\nVous avez utilisé {11 - i} tentatives\n")
else :
    print(f"\nVous avez épuisé vos tentatives.\nLa réponse était : {answer}\n")