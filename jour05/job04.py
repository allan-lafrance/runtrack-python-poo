def max_digit(liste, max_list=0):
    if liste == []:
        return max_list
    else:
        num = liste[0]
        if num > max_list:
            max_list = num
        return max_digit(liste[1:], max_list)

liste = [14, 38, 27, 49, 86, 1, 45, 65, 12]
max_list = max_digit(liste)
print(f"Le plus grand chiffre de la liste {liste} est : {max_list}")