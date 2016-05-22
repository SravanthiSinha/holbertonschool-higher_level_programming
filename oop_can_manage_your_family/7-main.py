from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
parents = marc.who_are_my_parents(my_family)
grandparents = marc.who_are_my_grand_parents(my_family)
print "My parents are %s" % (", ".join(map(str, parents)))
print "My grand parents are %s" % (", ".join(map(str, grandparents)))
print  (", ".join(map(str,grandparents[0].who_are_my_grandchildren(my_family))))
save_to_file(my_family, "my_family.json")
