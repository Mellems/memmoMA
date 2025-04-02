from random import choice

#list of 10 numbers and 5 letters
character = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

#name the winnning tickets
winner_winner = []
print("The ticket with these characters is the winner...")

#using while statement to select letters or numbers from the characters list.

while len(winner_winner) < 4:
    select_char = choice(character)

    if select_char not in winner_winner:
        print(f" The Character is {select_char}!")
        winner_winner.append(select_char)

