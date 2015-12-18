from distribution_model import DistributionModel
# from voting_system import VotingSystem
import election_control_algorithm as eca
from timeit import default_timer
# import signal


class Election:

    def make_election(self,
                      number_of_voters,
                      number_of_candidates,
                      distribution_model,
                      voting_system,
                      control_type):
        controlable = 0

        """Start Prepare elections"""
        dm = DistributionModel(number_of_voters, number_of_candidates)
        # set somehow distribution model in line below
        """
        possible distribution models:
        - polya_eggenberger
        - single_peaked_1d
        - single_peaked_2d
        """
        vp = getattr(dm, distribution_model)()

        """ Control start"""
        start = default_timer()

        """
        possible voting systems:
        - PluralityControl
        - BordaControl
        - CopelandControl
        - MaximinControl
        """
        control = getattr(eca, voting_system)(vp)
        controlable = getattr(control, control_type)()

        end = default_timer()
        running_time = end - start

        return controlable, running_time
