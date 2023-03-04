def length(chaine, count=0):
    if chaine == "":
        return count
    else:
        return length(chaine[1:], count+1)

chaine = str(input("Entrez un mot : "))
length = length(chaine)
print(f"La longueur de la chaîne '{chaine}' est : {length}")