import random as rd
import GUI
import Timer


# functions used in main module are placed below

def computer_choice() -> str:
    choice = rd.randint(1, 3)
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'


def round_number_converter(value):
    try:
        return int(value)
    except ValueError:
        print("Ha! You can't even choose a number let alone defeat me.")
        rounds = input("Choose an actual number: ")
        round_number_converter(rounds)


# user establishes the number of rounds prior to starting the game
print("Ah, so you think you can beat a hardcore veteran like me at Rock Paper Scissors? ")
Timer.countdown(3)
num_of_rounds = round_number_converter(input("How many times do you want to play me? I won't go easy on you. "))
while (num_of_rounds > 100) or (num_of_rounds < 0) or (num_of_rounds % 2 == 0):
    if num_of_rounds > 100:
        num_of_rounds = round_number_converter(input("I don't have all day! Choose a lower number of rounds: "))
    elif num_of_rounds < 0:
        num_of_rounds = round_number_converter(input("Ha ha. Very funny. Now choose an actual number of rounds: "))
    elif num_of_rounds % 2 == 0:
        num_of_rounds = round_number_converter(input("Only cowards allow for a possible draw! Choose an odd number: "))
print("Hmm ok... prepare to meet your doom!")
# Game is now initialized
win_counter = 0
loss_counter = 0
for round_number in range(1, num_of_rounds + 1):
    print("Rock")
    Timer.countdown(1)
    print("Paper")
    Timer.countdown(1)
    print("Scissors")
    Timer.countdown(1)
    user_choice = input("Make your choice: ")
    comp_choice = computer_choice()
    print("Shoe!")
    if user_choice == 'Rock':
        if comp_choice == 'Scissors':
            win_counter += 1
            GUI.display_win(round_number)
        elif comp_choice == 'Paper':
            loss_counter += 1
            GUI.display_loss(round_number)
        else:
            GUI.display_draw(round_number)
            continue
    elif user_choice == 'Paper':
        if comp_choice == 'Rock':
            win_counter += 1
            GUI.display_win(round_number)
        elif comp_choice == 'Scissors':
            loss_counter += 1
            GUI.display_loss(round_number)
        else:
            GUI.display_draw(round_number)
            continue
    elif user_choice == 'Scissors':
        if comp_choice == 'Paper':
            win_counter += 1
            GUI.display_win(round_number)
        elif comp_choice == 'Rock':
            loss_counter += 1
            GUI.display_loss(round_number)
        else:
            GUI.display_draw(round_number)
            continue
    else:
        loss_counter += 1
        GUI.display_loss(round_number)
        print("You didn't even make a valid choice... how sad.")
        Timer.countdown(1)
if win_counter > loss_counter:
    print("noooo...Nooooo... NOOOOOOO!!!")
    Timer.countdown(2)
    print("I have been defeated.")
    Timer.countdown(1)
    print("And so my reign has finally ended.")
elif win_counter < loss_counter:
    print("A valiant effort, but challenging a master such as myself was foolish from the start.")
    Timer.countdown(1)
    print("Perhaps one day you will get to my level. ")
else:
    print("WHATTT! IMPOSSIBLE! How could we have drawn! I THOUGHT WE HAD AVOIDED THIS.")
    Timer.countdown(2)
    print("Hmm.. perhaps you are a little better than I thought")
    Timer.countdown(1)
    print("Until we face each other again ... user")
