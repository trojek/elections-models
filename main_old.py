import yaml

from distribution_model import DistributionModel
from voting_system import VotingSystem
from election_control_algorithm import PluralityControl

# parameters (number_of_voters, number_of_candidates)
pe = DistributionModel(4, 4)
sp1d = DistributionModel(4, 4)
sp2d = DistributionModel(5, 5)

possible_votes = pe.generate_all_possible_preferences()

voters_preference = pe.polya_eggenberger(possible_votes)

voters_preferences_sp1d = sp1d.single_peaked_1d()
print voters_preferences_sp1d
print "---"
print sp1d.convert_voters_preferences_from_single_peaked_to_ranking(voters_preferences_sp1d)
print "---"

vs1 = VotingSystem(sp1d.convert_voters_preferences_from_single_peaked_to_ranking(voters_preferences_sp1d))
vs1prim = VotingSystem(voters_preference)
vs2 = VotingSystem(voters_preference)
vs3 = VotingSystem(voters_preference)
vs4 = VotingSystem(voters_preference)

print "Voters' preferences"
print voters_preference
print "Borda"
print vs1.borda()
print vs1prim.borda()
print "Plurality"
print vs2.pluarality()
print "Copeland"
print vs3.copeland()
print "Maximin"
print vs4.maximin()

print "------------------------------------"
print ""

pluralitycontrol = PluralityControl()
pluralitycontrol.ccdc()
