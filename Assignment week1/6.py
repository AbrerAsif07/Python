games_played = int(input("Enter number of games played = "))
games_won = int(input("Enter number of games won = "))
games_lost = int(input("Enter number of games lost = "))

games_tied = games_played - (games_won + games_lost)

total_points = (games_won * 4) + (games_tied * 2)
print(f"Number of games tied = {games_tied}")
print(f"Total points = {total_points}")
