import random

name = input("What is your name?")
print("Hello " + name)
gender = input(name + ", are you a boy/girl?")
if gender == "boy":
    pronoun = "He"
elif gender == "girl":
    pronoun = "She"
else:
    pronoun = "It"

names = ["Amitesh", "Amitanshu", "Aarav", "Krishna", "Tyrex", "Hiffo", "Oompa-Loompa"]
anames = ["Amitesh", "Amitanshu", "Aarav", "Krishna", "Tyrex", "Hiffo", "Oompa-Loompa"]
bnames = ["Amitesh", "Amitanshu", "Aarav", "Krishna", "Tyrex", "Hiffo", "Oompa-Loompa"]
roles = ["prince", "housefly","weed" , "banana peel", "ogre", "princess"]
aroles = ["prince", "housefly","weed" , "banana peel", "ogre", "princess"]
broles = ["prince", "housefly","weed" , "banana peel", "ogre", "princess"]
actions = ["rescue", "eat", "lick", "marry", "slay", "hypnotize"]
places = ["Dholakpur", "South Pole", "Underpants", "Bikini Bottom" ]

actor_name = random.choice(names)
aactor_name = random.choice(anames)
bactor_name = random.choice(bnames)
actor_role = random.choice(roles)
aactor_role = random.choice(aroles)
bactor_role = random.choice(broles)
quest = random.choice(actions)
magic_place = random.choice(places)

story = "Once upon a time, there was a " + actor_role + " called " + name + ". " + pronoun + " and some friends found themselves in the land of " + magic_place + ". This land was ruled by " + aactor_name + " the " + aactor_role + ". Suddenly, a mysterious voice spoke from inside " + name + "'s stomach- You must " + quest + " " + bactor_name + " the " + bactor_role + " to return back to your homes..."

print(story)
