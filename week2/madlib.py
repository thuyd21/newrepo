# mad lib word game 
# rules:
# one player acts as the reader
# They ask the other players, who have no knowledge of the story, to fill in the blanks by choosing adjectives, nouns, verbs, etc. The result is a funny story

#user input
name = input("enter your name: ")
noun = input("enter noun: ")
verb = input ("enter verb: ")
noun2 = input("enter noun: ")

#madlib sentence  
#"Hey! Welcome to my ____noun___. Here, we __verb_,about ___noun2___.
madlib = f"Hey!,{name}, Welcome to my {noun}. Here, we love to {verb} about {noun2}."


print(madlib)

