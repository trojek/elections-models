from distribution_model import DistributionModel
from voting_system import VotingSystem


class PluralityControl:

    def __init__(self):
        dm = DistributionModel(4, 4)
        possible_votes = dm.generate_all_possible_preferences()
        self.voters_preferences = dm.polya_eggenberger(possible_votes)
        self.vs = VotingSystem(self.voters_preferences)

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        pass

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
