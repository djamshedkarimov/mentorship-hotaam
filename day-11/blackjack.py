import random
from art import logo

def deal_card():
  #deals random card
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  #calculates total score
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    # checks if there is ace and prevents player from busting (going over limit)
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  # compares user's score and computer's score
  if user_score > 21 and computer_score < 21:
    return "you went over. loser"


  if user_score == computer_score:
    # just a bunch of if statement that represents who wins
    return "draw"
  elif computer_score == 21:
    return "haha opponent has blackjack"
  elif user_score == 21:
    return "win with blackjack"
  elif user_score > 21:
    return "you went over, lose"
  elif computer_score > 21:
    return "opponent went over, you win!"
  elif user_score > computer_score:
    return "win"
  else:
    return "lose"

def play_game():
  # start game

  print(logo)

# variables to start
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    # gets starting cards
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    # calculates score of user and player
    # also prints it
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   your cards: {user_cards}, current score: {user_score}")
    print(f"   computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      # checks if score is over limit or just 0
      is_game_over = True
    else:
      user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
      # get another card (random)
      if user_should_deal == "y":
        user_cards.append(deal_card())
        # gets another card
      else:
        is_game_over = True
              #ends game

  while computer_score != 0 and computer_score < 17:
    # computer gets cards until score is bigger than 17
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   your final hand: {user_cards}, final score: {user_score}")
  print(f"   computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  #compares the two scores

while input("do you want to play a game of blackjack? type 'y' or 'n': ") == "y":
  # asks if want to play game
  print("\n")
  play_game()
