import yaml

from distribution_models import DistributionModels
from voting_systems import VotingSystems
from election_control_algorithms import PluralityControl

# parameters (number_of_voters, number_of_candidates)
pe = DistributionModels(4,4)
sp1d = DistributionModels(4,4)
sp2d = DistributionModels(5,5)

possible_votes = pe.generate_all_possible_votes("whatever")
election = pe.polya_eggenberger(possible_votes, 0)

# print yaml.dump(election)

print yaml.dump(sp1d.single_peaked_1d())

# print yaml.dump(sp2d.single_peaked_2d())

vs1 = VotingSystems(election)
vs2 = VotingSystems(election)
vs3 = VotingSystems(election)
vs4 = VotingSystems(election)

print election
print "Borda"
print vs1.borda()
print "Plurality"
print vs2.pluarality()
print "Copeland"
print vs3.copeland()
print "Maximin"
print vs4.maximin()

pluralitycontrol = PluralityControl()
pluralitycontrol.ccdc()
