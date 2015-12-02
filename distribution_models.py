import random
import itertools
import math


class DistributionModels:

    def __init__(self, number_of_voters, number_of_candidates):
        self.nov = number_of_voters
        self.noc = number_of_candidates
        self.preferences = {}

    def polya_eggenberger(self, all_possible_votes, b):
        """Simulates Polya-Eggenberger urn model (Impartial Culture for b = 0)
        """
        for i in range(0, self.nov):
            drawn_vote = self.draw_vote(all_possible_votes)
            self.preferences["v" + str(i + 1)] = drawn_vote
            for _ in range(b):
                all_possible_votes.append(drawn_vote)
        return self.preferences

    def impartial_culture():
        return 0

    def single_peaked_1d(self):
        candidates = self.generate_random_positions_1d(self.noc)
        voters = self.generate_random_positions_1d(self.nov)
        candidates.sort()
        
        for i, voter in enumerate(voters, start=1):
            self.preferences["v" + str(i)] = {}
            for j, candidate in enumerate(candidates, start=1):
                self.preferences["v" + str(i)]["c" + str(j)
                                               ] = self.count_distance_1d(voter, candidate)

        return self.preferences

    def single_peaked_2d(self):
        candidates = self.generate_random_positions_2d(self.noc)
        voters = self.generate_random_positions_2d(self.nov)

        for i, voter in enumerate(voters, start=1):
            self.preferences["v" + str(i)] = {}
            for j, candidate in enumerate(candidates, start=1):
                self.preferences[
                    "v" + str(i)]["c" + str(j)] = self.count_distance_2d(candidate, voter)

        return self.preferences

    def draw_vote(self, urn):
        return urn[random.randint(0, len(urn) - 1)]

    def count_distance_1d(self, a, b):
        return abs(a - b)

    def count_distance_2d(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def generate_random_positions_1d(self, number):
        list_of_positions = []
        for _ in range(number):
            list_of_positions.append(random.random())
        return list_of_positions

    def generate_random_positions_2d(self, number):
        list_of_positions = []
        for _ in range(number):
            list_of_positions.append((random.random(), random.random()))
        return list_of_positions

    def generate_all_possible_votes(self, voting_system):
        candidates = []
        for i in range(1, self.noc + 1):
            candidates.append("c" + str(i))

        return list(itertools.permutations(candidates))
