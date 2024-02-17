# mad lib word game 
# rules:
# one player acts as the reader
# They ask the other players, who have no knowledge of the story, to fill in the blanks by choosing adjectives, nouns, verbs, etc. The result is a funny story

#user input
name = input("enter your name: ")
LegendaryWeapon = input("enter a Legendary Weapon: ")
adjective = input("enter a adjective: ")
verb2 = input ("enter a verb: ")
evilcreature = input ("enter a evil creature: ")
verb3 = input ("enter a verb: ")
Country = input ("enter a country: ")
#madlib sentence  
#"Hey! Welcome to my ____noun___. Here, we __verb_,about ___noun2___.
#madlib = f"Hey!,{name}, Welcome to my {noun}. Here, we love to {verb} about {noun2}."

madlib1 = f"Princess {name}, armed with the {LegendaryWeapon}, on a {adjective} quest to {verb2} the {evilcreature} and {verb3} {Country}."

# using f-strings: print(f'{i}: {message}')
#print(madlib)
print(madlib1)

    