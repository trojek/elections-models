# import yaml

# from distribution_models import DistributionModels
# from voting_systems import VotingSystems
from election_control_algorithm import PluralityControl

pluralitycontrol = PluralityControl()
print pluralitycontrol.ccdc()


"""
def method (number_of_voters, number_of_candidates, distribution_model, voting_system, control_type)
controlable
return controlable (0 or 1)
"""
