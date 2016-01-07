from election import Election

test_election = Election()
print "Plurality"
print test_election.make_election(5, 5, "polya_eggenberger", "PluralityControl", "ccdc")
print test_election.make_election(5, 5, "polya_eggenberger", "PluralityControl", "dcdc")

print "Borda"
print test_election.make_election(5, 5, "polya_eggenberger", "BordaControl", "ccdc")
print test_election.make_election(5, 5, "polya_eggenberger", "BordaControl", "dcdc")

print "Copeland"
print test_election.make_election(5, 5, "polya_eggenberger", "CopelandControl", "ccdc")
print test_election.make_election(5, 5, "polya_eggenberger", "CopelandControl", "dcdc")

print "Maximin"
print test_election.make_election(5, 5, "polya_eggenberger", "MaximinControl", "ccdc")
print test_election.make_election(5, 5, "polya_eggenberger", "MaximinControl", "dcdc")
