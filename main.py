print("Do you want a free or a paid game?")
print("Enter 1 if you want a free game")
print("Enter 2 if you want a paid game")
free_or_paid_game = int(input("Enter your choice"))
if free_or_paid_game == 2:
    money = int(input("How much money do you have?"))
    print("Your balance is", money, "dollars")
else:
    print("h")



my_games = []
cost_of_the_game = 0



def buy_game():
    with open("games.txt", "r") as f:
        games = "\n".join(f.readlines())
    return games


def buy_free_game():
    with open("free_games.txt", "r") as f:
        free_games = "\n".join(f.readlines())
    return free_games


def add_game():
    if number_of_the_game == 1:
        my_games.append(name_of_the_game)
    elif number_of_the_game == 2:
        my_games.append(name_of_the_game)
    elif number_of_the_game == 3:
        my_games.append(number_of_the_game)
    else:
        my_games.append(name_of_the_game)

def delete_games:
    


print("Enter 1 if you want first game")
print("Enter 2 if you want second game")
print("Enter 3 if you want third game")
print("Enter 4 if you want fourth game")

name_of_the_game = buy_game()
print(name_of_the_game)
number_of_the_game = int(input("Enter your choice"))


if number_of_the_game == 1:
    print("Your choice is The Witcher 3")
elif number_of_the_game == 2:
    print("Your choice is The Sims 4")
elif number_of_the_game == 3:
    print("Your choice is Disco Elysium")
else:
    print("Your choice is Elden Ring")


add_game()
print(my_games)








# def delete_game
# def all_games
# def user_games





# def get_name():
#     with open("name.txt", "r") as f:
#         name = "\n".join(f.readlines())
#     return name