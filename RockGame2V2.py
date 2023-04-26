

# Input player names
player1 = input("Please, enter your name player 1: ")
player2 = input("Please, enter your name player 2: ")

# Initialize scores
score1 = 0
score2 = 0

#read name
# F-strings were introduced in Python 3.6 and provide a concise and efficient way to format strings.
# when you use f-string you can use curly braces

print(f"Welcome, {player1} and {player2}!")

# Play 3 rounds
for round in range(3):
    print(f"\nRound {round+1}:")

# Get players inputs
    choice1 = input(f"{player1}, choose rock (R), paper (P), or scissors (S): ").upper()
    choice2 = input(f"{player2}, choose rock (R), paper (P), or scissors (S): ").upper()

# Determine winner of the round
    if choice1 == choice2:
        print("Tie!")
    elif choice1 == "R" and choice2 == "S" or choice1 == "S" and choice2 == "P" or choice1 == "P" and choice2 == "R":
        score1 += 1
    else:
        score2 += 1

# Determine winner of the game
if score1 > score2:
    print(f"\n{player1} wins the game with {score1} points!")
elif score2 > score1:
    print(f"\n{player2} wins the game with {score2} points!")
else:
# If there is a tie in the 3 rounds end, play an extra round
    print("\nTie game! Playing an extra round...")
    choice1 = input(f"{player1}, choose rock (R), paper (P), or scissors (S): ").upper()
    choice2 = input(f"{player2}, choose rock (R), paper (P), or scissors (S): ").upper()

    if choice1 == choice2:
        print("Tie!")
    elif choice1 == "R" and choice2 == "S" or choice1 == "S" and choice2 == "P" or choice1 == "P" and choice2 == "R":
        print(f"{player1} wins the game with {score1+1} points!")
    else:
        print(f"{player2} wins the game with {score2+1} points!")


#Say thank you
print("Thank you for playing the game")
