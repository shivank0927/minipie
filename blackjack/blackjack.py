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
        deck = GetDeck()
        dealer = [deck.pop(), deck.pop()]
        player = [deck.pop(), deck.pop()]

        print("YOUR BET:", bet)
        while True:
            ShowHand(dealer, player, False)
            print()
            
            if GetValue(player) > 21:
                break
            move = GetMove(player, money - bet)
            
            if move == "D":
                ExtraBet = GetBet(min(bet, (money - bet)))
                bet += ExtraBet
                print(f"Bet Increased to {bet}")
                print(f"BET: {bet}")
            
            if move in ['H', 'D']:
                card = deck.pop()
                rank, suit = card
                print(f"YOU DREW {rank} OF {suit}")
                player.append(card)

                if GetValue(player) > 21:
                    continue # busted!
            
            if move in ['S', 'D']:
                break # time for the dealer

            


def ShowHand(cards):
    for card in cards():
        if card == BACKSIDE:
            print("HIDDEN CARD")
        else:
            rank, suit = card
            print(f"you have {rank} of {suit}")

def GetMove(player, money):
    while True:
        if len(player) == 2 and money > 0:
            move = input("""(H)IT TO TAKE ANOTHER CARD
                        (S)TAND TO STOP TAKING CARDS
                        (D)OUBLE DOWN {ONLY FOR FIRST TIME!}""")
            if move in ["H", "S", "D"]:
                return move
        else:
            move = input("""(H)IT TO TAKE ANOTHER CARD
                        (S)TAND TO STOP TAKING CARDS""")
            if move in ["H", "S"]:
                return move
            
def GetValue(cards):
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
def GetDeck():
    deck = []

    for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
        for rank in range(2, 11):
            deck.append((str(rank), suit))
    
    return random.shuffle(deck)

def GetBet(maxBet):
    while True:
        bet = input("How much you bet?, or type QUIT\n>>").upper().strip()
        if bet == "QUIT":
            sys.exit("END")
        
        if not bet.isdigit():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

