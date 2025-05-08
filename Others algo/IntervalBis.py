def decoupe_intervalles(intervals):
    # On récupère toutes les bornes et on les trie
    points = set()
    for start, end in intervals:
        points.add(start)
        points.add(end)
    sorted_points = sorted(points)

    # On crée les intervalles élémentaires entre les points adjacents
    elementary_intervals = []
    for i in range(len(sorted_points) - 1):
        a, b = sorted_points[i], sorted_points[i + 1]
        # On vérifie si [a, b] est couvert par au moins un intervalle initial
        is_covered = any(start < b and end > a for start, end in intervals)
        if is_covered:
            elementary_intervals.append((a, b))

    return elementary_intervals


if __name__ == '__main__':
    intervals = [(2, 8), (5, 12), (9, 22), (16, 20), (18, 25), (23, 28), (27, 35), (33, 40), (38, 42), (41, 50)]
    resultat = decoupe_intervalles(intervals)
    print(resultat)
