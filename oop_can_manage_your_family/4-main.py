from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]

if marc.is_married():
    print "Marc is married"

marc.just_married_with(vanessa)
if marc.is_married():
    print "Marc is NOW married"

# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
my_family.append(b)
marc.just_married_with(vanessa)

save_to_file(my_family,'new_family.json')
