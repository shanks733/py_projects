import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def count11(card_list):
    n = 0
    for card in card_list:
        if card ==11:
            n+=1
    return n
play = True

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
while play:
    win = False
    lose = False
    draw = False
    choice = input("do you want to play a game of blackjack .Type 'y' or 'n': ")
    if choice == 'n':
        break
    elif choice == 'y':
        pass
    else:
        print("enter a valid choice")
        continue
    print(logo)
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    comp_card1 = random.choice(cards)
    comp_card2 = random.choice(cards)
    player_score = card1+card2
    comp_score = comp_card1+comp_card2
    player_cards = [card1,card2]
    comp_cards = [comp_card1,comp_card2]
    count_11 = count11(player_cards)
    comp_count11 = count11(comp_cards)
    print(f"Your cards : [{card1},{card2}], current score: {player_score}")
    print(f"Computers first card: {comp_card1}")
    if player_score == 21:
        if comp_score == 21:
            print(f"Your final hand : [{player_cards}]")
            print(f"computers final hand : [{comp_cards}]")
            print("Its a draw")
            continue
        else:
            print(f"Your final hand : [{player_cards}]")
            print(f"computers final hand : [{comp_cards}]")
            print("You won")
            continue
    if comp_score == 21:
        print(f"Your final hand : [{player_cards}]")
        print(f"computers final hand : [{comp_cards}]")
        print("computer wins")
        continue

    while True:
        hit = input("Type 'y' to hit 'n' to stand :")
        if hit == 'n':
            while comp_score <=16:
                comp_newcard = random.choice(cards)
                if comp_newcard ==11:
                    comp_count11 += 1
                comp_cards.append(comp_newcard)
                comp_score += comp_newcard
                if comp_score > 21:
                    if comp_count11>0:
                        comp_score-=10
                        comp_count11 -=1
                        continue
                    print(f"Your final hand : [{player_cards}]")
                    print(f"computers final hand : [{comp_cards}]")
                    print("computer went bust...you won")
                    win = True
                    break
            if win == True:
                break
            if player_score > comp_score:
                print(f"Your final hand : [{player_cards}]")
                print(f"computers final hand : [{comp_cards}]")
                print("You won")
                break
            elif player_score == comp_score:
                print(f"Your final hand : [{player_cards}]")
                print(f"computers final hand : [{comp_cards}]")
                print("Its a draw")
                break
            elif player_score < comp_score and win == False:
                print(f"Your final hand : [{player_cards}]")
                print(f"computers final hand : [{comp_cards}]")
                print("computer wins")
                break
        elif hit == 'y':
            new_card = random.choice(cards)
            if new_card ==11:
                count_11 +=1
            player_score += new_card
            player_cards.append(new_card)
            print(f"Your hand : [{player_cards}]")
            if player_score > 21:
                if count_11 > 0:
                    player_score -= 10
                    count_11 -= 1
                    continue
                print(f"Your final hand : [{player_cards}]")
                print(f"computers final hand : [{comp_cards}]")
                print("You went over.....you lost")
                lose = True
                break
            elif player_score == 21:
                print(f"Your final hand : [{player_cards}]")
                print(f"computers final hand : [{comp_cards}]")
                print("you won")
                break






