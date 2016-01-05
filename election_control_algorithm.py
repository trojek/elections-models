from distribution_model import DistributionModel
from voting_system import VotingSystem
import random


class PluralityControl:

    def __init__(self, voters_preferences):
        self.vs = VotingSystem(voters_preferences)

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        self.candidates_ranking = self.vs.pluarality()
        denoted_candidate = random.choice(self.candidates_ranking[1:])
        controlable = 0

        # execption handling - for empty list
        while True:
            self.candidates_ranking.pop(0)
            if self.candidates_ranking[0] == denoted_candidate:
                controlable = 1
                break

        return controlable

    def dcdc(self):
        self.candidates_ranking = self.vs.pluarality()
        candidates_ranking_base = list(self.candidates_ranking)

        controlable = 0

        # execption handling - for empty list
        while True:
            self.candidates_ranking.pop(0)
            if candidates_ranking_base[0][0] != self.candidates_ranking[0][0]:
                controlable = 1
                break

        return controlable


class BordaControl:

    def ccac():
        pass

    def dcac():
        pass

    def ccdc():
        pass

    def dcdc():
        pass

    def ccav():
        pass

    def dcav():
        pass

    def ccdv():
        pass

    def dcdv():
        pass


class CopelandControl:

    def ccac(ranking_list, list_of_preferences, bound_k):
        pass

    def dcac():
        pass

    def ccdc():
        pass

    def dcdc():
        pass

    def ccav():
        pass

    def dcav():
        pass

    def ccdv():
        pass

    def dcdv():
        pass


class MaximinControl:

    def ccac(ranking_list, list_of_preferences, bound_k):
        pass

    def dcac():
        pass

    def ccdc():
        pass

    def dcdc():
        pass

    def ccav():
        pass

    def dcav():
        pass

    def ccdv():
        pass

    def dcdv():
        pass
