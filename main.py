import csv
import random

def read_file():
  f = open('megasena.csv', 'r')
  reader = csv.reader(f, delimiter=',')
  counter = {} 
  games = []
  for row in reader:
    game = []
    for n in row[0:6]:
      game.append(int(n))
    games.append(game)
    for i in range(6):
      number = row[i]
      if number in counter:
        counter[number] += 1
      else:
        counter[number] = 1
  sorted_numbers = sorted(counter.items(), key=lambda x:x[1])
  return games

def random_game(n, g):
  games = []
  numbers = range(60)
  for _ in range(g):
    game = random.sample(numbers, n)
    games.append(game)
  return games

def check_game(game, games):
  count = 1
  winning = 0
  for past_game in games:
    hits = 0
    for n in past_game:
      if n in game:
        hits += 1
    if hits == 6:
      print(f"({count}) Big Win!: {game} - {past_game}")
    elif hits == 5:
      print(f"({count}) Almost, 5 hits!: {game} - {past_game}")
    elif hits == 4:
      print(f"({count}) Not bad, 4 hits!: {game} - {past_game}")
    if hits >= 4:
      winning += 1
    count += 1
  if winning > 0:
    print(f'Winnings: {winning}')
  print('--------')

      


def main():
  past_games = read_file()
  games = random_game(7, 100)
  c = 1
  for game in games:
    print(f'checking game {c} - {game}')
    c += 1
    check_game(game, past_games)
    print('---------')

def checking_doubles():
  past_games = read_file()
  c = 1
  for p1 in past_games:
    print(f'checking game {c}')
    check_game(p1, past_games)
    c += 1

main()
#checking_doubles()
  







