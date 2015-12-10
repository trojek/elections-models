from distribution_model import DistributionModel
from voting_system import VotingSystem


class PluralityControl:

    def __init__(self):
        dm = DistributionModel(4, 4)
        possible_votes = dm.generate_all_possible_votes("voting system")
        self.voters_preferences = dm.polya_eggenberger(possible_votes)
        self.vs = VotingSystem(self.voters_preferences)

    def ccac(list_of_preferences):
        pass

    def dcac():
        pass

    def ccdc(self):
        self.candidates_ranking = self.vs.pluarality()
        print self.voters_preferences
        print self.candidates_ranking

    def dcdc():
        pass


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
