class Solution():
    def polymerization(self, polymer, rules, ite):
        polymer = [char for char in polymer]
        for _ in range(ite):
            newPolymer = []
            for i in range(len(polymer) - 1):
                newPolymer.append(polymer[i])
                newPolymer.append(rules[polymer[i] + polymer[i + 1]])
            polymer = newPolymer + [polymer[len(polymer) - 1]]
        polymerSet = set(polymer)
        max = 0
        min = float('inf')
        for a in polymerSet:
            nb = polymer.count(a)
            if nb > max:
                max = nb
            elif nb < min:
                min = nb
        return max - min

    def polymerization2(self, polymer, rules, ite):
        for _ in range(ite):
            newPolymer = ""
            for i in range(len(polymer) - 1):
                newPolymer += polymer[i] + rules[polymer[i] + polymer[i + 1]]
            polymer = newPolymer + polymer[len(polymer) - 1]
        polymerSet = set(polymer)
        max = 0
        min = float('inf')
        for a in polymerSet:
            nb = polymer.count(a)
            if nb > max:
                max = nb
            elif nb < min:
                min = nb
        return max - min

    def polymerization3(self, polymer, rules, ite):
        pairs = {}
        for i in range(len(polymer) - 1):
            if polymer[i] + polymer[i+1] not in pairs:
                pairs[polymer[i] + polymer[i+1]] = 1
            else:
                pairs[polymer[i] + polymer[i+1]] += 1

        for _ in range(ite):
            pairsIte = {}
            for pair in pairs:
                firstPair = pair[0]+rules[pair]
                secondPair = rules[pair]+pair[1]
                if firstPair not in pairsIte:
                    pairsIte[firstPair] = pairs[pair]
                else:
                    pairsIte[firstPair] += pairs[pair]
                if secondPair not in pairsIte:
                    pairsIte[secondPair] = pairs[pair]
                else:
                    pairsIte[secondPair] += pairs[pair]
            pairs = pairsIte.copy()
        nbLetter = {}
        for pair in pairs:
            if pair[0] not in nbLetter:
                nbLetter[pair[0]] = 1 * pairs[pair]
            else:
                nbLetter[pair[0]] += 1 * pairs[pair]

        if polymer[len(polymer)-1] not in nbLetter:
            nbLetter[polymer[len(polymer)-1]] = 1
        else:
            nbLetter[polymer[len(polymer) - 1]] += 1

        nbLetter = list(nbLetter.values())

        return max(nbLetter)-min(nbLetter)


if __name__ == "__main__":
    rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C',
             'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B',
             'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
    polymer = "NNCB"
    ite = 40
    solution = Solution()
    print(solution.polymerization3(polymer, rules, ite))
