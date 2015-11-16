import yaml

from distribution_models import DistributionModels

# parameters (number_of_voters, number_of_candidates)
pe = DistributionModels(3,3)
sp1d = DistributionModels(4,4)
sp2d = DistributionModels(5,5)

array = pe.generate_all_possible_votes(1)

print yaml.dump(pe.polya_eggenberger(array, 0))

print yaml.dump(sp1d.single_peaked_1d())

print yaml.dump(sp2d.single_peaked_2d())
