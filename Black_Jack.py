#100 Days of Code, Dr. Angela Yu, Day11, Black Jack Project,
#Student: Łukasz Świątek Brzeziński

#Difficulty level: normal
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score.
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#Hint 13: Create a function called compare() and pass in the user_score and computer_score.
#If the computer and user both have the same score, then it's a draw.
#If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins.
#If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
#If none of the above, then the player with the highest score wins.
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
   

import random

def deal_card():
    '''choose one random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(List_of_cards):
    '''Take a list of cards and return the score calculated from the cards'''
    score = sum(List_of_cards)
    if len(List_of_cards) == 2 and score == 21:
        score = 0
    if 11 in List_of_cards == True and score > 21:
        List_of_cards[List_of_cards.index(11)] = 1 
    return score
    
def compare(user_score, computer_score):
    '''Contains all of the game conditionals, looking for the result. Who win'''
    if user_score == computer_score:
        print("It's a draw")
    elif computer_score == 0:
        print("The computer has a blackjack (0), you lose")
    elif user_score == 0:
        print("You have a blackjack (0), you win")
    elif user_score > 21:
        print("You went over. You lose :(")
    elif computer_score > 21:
        print("Computer wents over. You win :)")
    elif computer_score > user_score:
        print("Computer wins")
    elif user_score > computer_score:
        print("You win")   

restart = input("do you want to play BlackJack (y, n)? ").strip().lower()


while restart == 'y':

    user_cards = []
    computer_cards = []

    for element in range(2):
        user_cards.append(deal_card())
    for element in range(2):
        computer_cards.append(deal_card())
     

    move = True
    while move:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("\n")
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print("Computer's first card: {}".format(computer_cards[0]))
        print("\n")
        if user_score > 21:
            print("You went over. You lose :(")
            break
        elif user_score == 0 or computer_score > 21:
            print("you Win!!!")
            break
    
        player_move = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
        if player_move == 'y':
            user_cards.append(deal_card())
        else:
            move = False


    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print("Computer's cards: {}, computers score: {}".format(computer_cards, computer_score))
    compare(user_score, computer_score)

    restart = input("Do you want to play again? (y, n)").strip().lower()
    if restart == 'n':
        print("Good bye!")
        break
             


        
    #---------------------------------------------------LVL EXPERT (preliminary work without upper hints)--------------------------------------------------
    
    ##import random
##
##cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
##
##Player_cards = []
##Comp_cards = []
##Player_hand = 0
##Comp_hand = 0   
##
##
##def score():
##    print(f"Your cards: {Player_cards}, current score: {Player_hand}")
##    print("Computer's first card: {}".format(Comp_cards))
##    
##def final_score():
##    print("Your final hand: {}, final score: {}".format(Player_cards, Player_hand))
##    print("Computer's final hand: {}, final score {}".format(Comp_cards, Comp_hand))
##
##def win_rules():
##    if Player_hand > Comp_hand:
##        print("you Win!!!")
##    elif Comp_hand > Player_hand:
##        print("You went over. You lose :(")
##    else:
##        print("It's a draw")
##
##def add_card(player):
##    '''function to add the points. player = list'''
##    choice = random.choice(cards)
##    player = player.append(choice)
##    return player
##    
##
##
##if Player_hand > 10 or Comp_hand > 10:
##    cards[0] = 1
##    
##Start_game = input("do you want to play game of blackjack? (y, n): ").strip().lower()
##if Start_game == "y":
####    for element in range(2):
####        Player_choice = random.choice(cards)
####        Player_cards.append(choice)
####        Player_hand += Player_choice
####    Comp_choice = random.choice(cards)
####    Comp_cards.append(Comp_choice)
####    Comp_hand += Comp_choice
##    add_card(Player_cards)
##    add_card(Player_cards)
##    Player_hand = 0
##    for element in Player_cards:
##        Player_hand += element
##    add_card(Comp_cards)
##    score()
##    
##    
##    player_move = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
##    
##    while player_move == 'y':
##        
##        if Player_hand > 21:
##            final_score()
##            print("You went over. You lose :(")
##            break
##        add_card(Player_cards)
##        Player_hand = 0
##        for element in Player_cards:
##            Player_hand += element
##        score()
##        if Player_hand > 21:
##            final_score()
##            break
##        player_move = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
##        
##
##while Comp_hand < Player_hand:
##    add_card(Comp_cards)
##    Comp_hand = 0
##    for element in Comp_cards:
##        Comp_hand += element
##if Comp_hand > 21:
##    final_score()
##    print("You went over. You lose :(")
##elif Comp_hand > Player_hand or (Comp_hand == Player_hand and Comp_hand <= 14):
##    final_score()
##    print("You went over. You lose :(")
##elif Comp_hand == Player_hand and Comp_hand > 14:
##    final_score()
##    print("It's a draw")
##        
##  
##    
##    

    
    
