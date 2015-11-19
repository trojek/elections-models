import itertools

class VotingSystems:

    candidates_points = {}

    def __init__(self, preferences):
        self.preferences = preferences
        self.candidates_points = self.prepare_list_of_candidates()

    def borda(self):
        max_points = len(self.preferences.values()[0])

        for voter, voters_preference in self.preferences.iteritems():
            points = max_points - 1
            for single_preference in voters_preference:
                self.candidates_points[single_preference] += points
                points -= 1

        return self.candidates_points

    def copeland(self):
        pair_comparison = self.generate_pairs_for_pairwise_comparison()
        pair_comparison = self.compare_pairs(pair_comparison)
        self.count_candidate_points(pair_comparison)

        return self.candidates_points

    def maximin(self):
        pair_comparison = list(itertools.permutations(self.preferences.values()[0],2))
        list_of_candidates = self.preferences.values()[0]

        # Compare all pairs
        list_of_results = {}
        for pair in pair_comparison:
            result = 0
            for key, value in self.preferences.iteritems():
                if value.index(pair[0]) < value.index(pair[1]):
                    result +=1
                else:
                    result -=1
            list_of_results[pair] = result

        # Take min value from compared pairs
        final_results = {}
        for candidate in list_of_candidates:
            results = []
            for key, value in list_of_results.iteritems():
                if key[0] == candidate:
                    results.append(value)
                    final_results[key[0]] = min(results)

        return final_results

    def pluarality(self):
        for voter, voters_preference in self.preferences.iteritems():
                self.candidates_points[voters_preference[0]] += 1

        return self.candidates_points

    def prepare_list_of_candidates(self):
        list = {}
        for value in self.preferences.values()[0]:
            list[value] = 0
        return list

    def generate_pairs_for_pairwise_comparison(self):
        pairs = []
        combinations = list(itertools.combinations(self.preferences.values()[0],2))
        for pair in combinations:
            pairs.append({pair[0]: 0, pair[1]: 0})

        return pairs

    def compare_pairs(self, pair_comparison):
        for pair in pair_comparison:
            for key, value in self.preferences.iteritems():
                if value.index(pair.keys()[0]) < value.index(pair.keys()[1]):
                    pair[pair.keys()[0]] +=1
                else:
                    pair[pair.keys()[1]] +=1

        return pair_comparison

    def count_candidate_points(self, pair_comparison):
        for pair in pair_comparison:
            if pair.values()[0] > pair.values()[1]:
                self.candidates_points[pair.keys()[0]] += 1
            else:
                self.candidates_points[pair.keys()[1]] += 1
