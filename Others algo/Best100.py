import random


def find_min(l):
    min_val = l[0]
    min_idx = 0
    for i in range(1, len(l)):
        if l[i] < min_val:
            min_val = l[i]
            min_idx = i
    return min_val, min_idx


def top_max(liste, n):
    # Prendre les n premiers éléments comme candidats
    top = liste[:n]

    # Parcourir le reste de la liste
    for x in liste[n:]:
        min_val, min_idx = find_min(top)
        if x > min_val:
            top[min_idx] = x  # Remplacer le plus petit

    return top


if __name__ == "__main__":
    # Générer une liste de 1000 entiers aléatoires entre 1 et 5000 (avec répétitions)
    liste_nombres = [random.randint(1, 5000) for _ in range(1000)]
    print(liste_nombres)
    resultat = top_max(liste_nombres, 100)
    print(resultat)
