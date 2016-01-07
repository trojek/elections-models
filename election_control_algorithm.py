from voting_system import VotingSystem
import random


class PluralityControl:
    def __init__(self, voters_preferences):
        self.vs = VotingSystem(voters_preferences)
        self.method = "plurality"

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        return ccdc_universal(self)

    def dcdc(self):
        return dcdc_universal(self)


class BordaControl:
    def __init__(self, voters_preferences):
        self.vs = VotingSystem(voters_preferences)
        self.method = "borda"

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        return ccdc_universal(self)

    def dcdc(self):
        return dcdc_universal(self)

    def ccav(self):
        pass

    def dcav(self):
        pass

    def ccdv(self):
        pass

    def dcdv(self):
        pass


class CopelandControl:
    def __init__(self, voters_preferences):
        self.vs = VotingSystem(voters_preferences)
        self.method = "copeland"

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        return ccdc_universal(self)

    def dcdc(self):
        return dcdc_universal(self)

    def ccav(self):
        pass

    def dcav(self):
        pass

    def ccdv(self):
        pass

    def dcdv(self):
        pass


class MaximinControl:
    def __init__(self, voters_preferences):
        self.vs = VotingSystem(voters_preferences)
        self.method = "maximin"

    def ccac(self):
        pass

    def dcac(self):
        pass

    def ccdc(self):
        return ccdc_universal(self)

    def dcdc(self):
        return dcdc_universal(self)

    def ccav(self):
        pass

    def dcav(self):
        pass

    def ccdv(self):
        pass

    def dcdv(self):
        pass


def ccdc_universal(self):
    self.candidates_ranking = getattr(self.vs, self.method)()
    denoted_candidate = random.choice(self.candidates_ranking[1:])
    controlable = 0

    # execption handling - for empty list
    while True:
        self.candidates_ranking.pop(0)
        if self.candidates_ranking[0] == denoted_candidate:
            controlable = 1
            break

    return controlable


def dcdc_universal(self):
    self.candidates_ranking = getattr(self.vs, self.method)()
    candidates_ranking_base = list(self.candidates_ranking)

    controlable = 0

    # execption handling - for empty list
    while True:
        self.candidates_ranking.pop(0)
        if candidates_ranking_base[0][0] != self.candidates_ranking[0][0]:
            controlable = 1
            break

    return controlable
