import random


def game_win(user, computer):
    if user == computer:
        return None
    
    #Sanke vs water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False
    
    #Water vs Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False
    
    # Gun Vs Snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


ran_no = random.randint(1, 3)



print("computer's turn: snake(s), Water(w), Gun (g)")
if ran_no == 1:
    computer = "s"
elif ran_no == 2:
    computer = "w"
else:
    computer = "g"

user = input("your's turn: snake(s), Water(w), Gun (g) ").lower()


result = game_win(user, computer) #Returns true if you win, False for lose, none for draw
print(f"\nYou chose: {user}")
print(f"\nComputer chose: {computer}")

if result is None:
    print("Its a draw!")

elif(result):
    print("You win!")
else:
    print("You lose!")