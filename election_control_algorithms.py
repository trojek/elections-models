from distribution_models import DistributionModels
from voting_systems import VotingSystems

class PluralityControl:

    def __init__(self):
        dm = DistributionModels(4,4)
        possible_votes = dm.generate_all_possible_votes("whatever")
        election = dm.polya_eggenberger(possible_votes, 0)
        vs = VotingSystems(election)

        self.candidates_ranking = vs.pluarality()
        self.voters_preferences = election

    def ccac(list_of_preferences):

        pass

    def dcac():
        pass

    def ccdc(self):
        print self.candidates_ranking
        print self.voters_preferences

    def dcdc():
        self.candidates_ranking.pop(0)

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
