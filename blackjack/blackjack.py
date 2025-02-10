import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'back'

def main():
    print("""The Blackjack\n
          Rules:\n
                Try to get as close to 21 without going over
                Kings, Queens and Jacks are worth 10 points
                Aces are worth 1 or 11 points
                Cards from 2 to 10 are worth their face value
                (H)it to take another card
                (S)tand to stop taking cards
                On your first play, you can (D)ouble down to increase your bet
                If tie occurs, the bet will be returned to the player
                The dealer stops hitting at 17""")
    
    money = 5000
    while True:
        if money <= 0:
            sys.exit("YOU ARE BROKE")
        
        bet = GetBet(money)
        print(f"YOU HAVE {money} Rs.")
        deck = GetDeck()
        dealer = [deck.pop(), deck.pop()]
        player = [deck.pop(), deck.pop()]

        print("YOUR BET:", bet)

        while True:
            ShowHand(dealer, True)   
            ShowHand(player, False)  
            print()
            
            if GetValue(player) > 21:
                break  # player busted
            
            move = GetMove(player, money - bet)
            
            if move == "D":
                ExtraBet = GetBet(min(bet, (money - bet)))
                bet += ExtraBet
                print(f"Bet Increased to {bet}")
            
            if move in ['H', 'D']:
                card = deck.pop()
                rank, suit = card
                print(f"YOU DREW {rank} OF {suit}")
                player.append(card)

                if GetValue(player) > 21:
                    continue  # player busted
            
            if move in ['S', 'D']:
                break  

        if GetValue(player) <= 21:
            while GetValue(dealer) < 17:
                print("\nDEALER HITS!")
                dealer.append(deck.pop())
                ShowHand(dealer, True)  # dealer's card

                if GetValue(dealer) > 21:
                    break  # dealer busted

                input("\nPress ENTER to continue...\n")

        
        ShowHand(dealer, False)
        ShowHand(player, False)  

        ppts = GetValue(player)
        dpts = GetValue(dealer)

        if dpts > 21:
            print(f"\nDEALER'S BUSTED! YOU WIN {bet} Rs.")
            money += bet
        elif ppts > 21 or ppts < dpts:
            print("\nYOU LOST")
            money -= bet
        elif ppts == dpts:
            print("\nIT'S A TIE")

        input("\nENTER to continue...\n")

def ShowHand(cards, dealer=False): # function to reveal the card of dealer/player

    if dealer:
        print("\nDEALER'S HAND:")
    else:
        print("\nYOUR HAND:")
    
    for i, card in enumerate(cards):
        if i == 0 and dealer:
            print("HIDDEN CARD")
        else:
            rank, suit = card
            print(f"{rank} of {suit}")
    print()

def GetMove(player, money): # for hit, stand, double down validation

    while True:
        if len(player) == 2 and money > 0:
            move = input("\n(H)IT, (S)TAND, or (D)OUBLE DOWN? ").upper().strip()
            if move in ["H", "S", "D"]:
                return move
        else:
            move = input("\n(H)IT or (S)TAND? ").upper().strip()
            if move in ["H", "S"]:
                return move

def GetValue(cards): # calculation of points of cards dealt

    value = 0
    aces = 0
    for card in cards:
        rank = card[0]
        
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == "A":
            aces += 1
            value += 11  
    
    while value > 21 and aces:
        value -= 10  
        aces -= 1
    
    return value 

def GetDeck(): # func. to get a shuffled deck

    deck = []
    for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
        for rank in list(map(str, range(2, 11))) + ['J', 'Q', 'K', 'A']:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def GetBet(maxBet): # prompting user for betting the money

    while True:
        bet = input("\nHow much do you bet? or type QUIT) -->> ").upper().strip()
        if bet == "QUIT":
            sys.exit("\nGAME OVER!")
        
        if not bet.isdigit():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

if __name__ == "__main__":
    main()
