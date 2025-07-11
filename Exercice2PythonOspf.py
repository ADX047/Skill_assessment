def nombre_contiguite_ospf(nombre_routeurs):
    """
    Calcule le nombre de voisinages OSPF qu'un routeur doit avoir dans une zone à accès multiple.

    :param nombre_routeurs: int, nombre total de routeurs dans la zone
    :return: int, nombre de voisinages nécessaires pour un routeur
    """
    if nombre_routeurs < 2:
        return 0  # Pas de voisinage possible avec un seul routeur
    return nombre_routeurs - 1

# Exemple d'utilisation :
print(nombre_contiguite_ospf(5))  # Résultat : 4
