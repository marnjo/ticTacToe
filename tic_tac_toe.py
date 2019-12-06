import sys 
import random
played = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" ",}
moves = [1,2,3,4,5,6,7,8,9]
playedMoves = []

def playerOne(played,moves,playedMoves):
  ruleBoard()
  drawBoard(played)
  choice = int(input("Player one's turn: "))
  if choice in moves:
    moves.remove(choice)
    playedMoves.append(choice)
    print(moves,played,playedMoves)
    played[choice] = "X"
    if played[1] == "X" and played[2] == "X" and played[3] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[2] == "X" and played[5] == "X" and played[8] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[3] == "X" and played[6] == "X" and played[9] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[1] == "X" and played[4] == "X" and played[7] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[4] == "X" and played[5] == "X" and played[6] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[3] == "X" and played[5] == "X" and played[7] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[1] == "X" and played[5] == "X" and played[9] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[7] == "X" and played[8] == "X" and played[9] == "X":
      print("PLayer One wins!!!!!")
      drawBoard(played)
      sys.exit()
  else:
    print("invalid move :(")
    playerOne(played,moves,playedMoves)

def playerTwo(played,moves,playedMoves):
  ruleBoard()
  drawBoard(played)
  choice = int(input("Player two's turn: "))
  if choice in moves:
    moves.remove(choice)
    playedMoves.append(choice)
    played[choice] = "O"
    if played[1] == "O" and played[2] == "O" and played[3] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[2] == "O" and played[5] == "O" and played[8] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[3] == "O" and played[6] == "O" and played[9] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[1] == "O" and played[4] == "O" and played[7] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[4] == "O" and played[5] == "O" and played[6] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[3] == "O" and played[5] == "O" and played[7] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[1] == "O" and played[5] == "O" and played[9] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
    if played[7] == "O" and played[8] == "O" and played[9] == "O":
      print("PLayer Two wins!!!!!")
      drawBoard(played)
      sys.exit()
  else:
    print("Invalid MOve :(")
    playerTwo(played,moves,playedMoves)

def compPlay(played,moves,playedMoves):
  if played[1] == "O" and played[2] == "O":
    if 3 in moves:
      choice = 3
  elif played[1] == "O" and played[3] == "O":
    if 2 in moves:
      choice = 2
  elif played[2] == "O" and played[3] == "O":
    if 1 in moves:
      choice = 1
  elif played[2] == "O" and played[5] == "O":
    if 8 in moves:
      choice = 8
  elif played[5] == "O" and played[8] == "O":
    if 2 in moves:
      choice = 2
  elif played[2] == "O" and played[8] == "O":
    if 5 in moves:
      choice = 5
  elif played[3] == "O" and played[6] == "O":
    if 5 in moves:
      choice = 5
  elif played[3] == "O" and played[5] == "O":
    if 6 in moves:
      choice = 6
  elif played[6] == "O" and played[5] == "O":
    if 3 in moves:
      choice = 3
  elif played[1] == "O" and played[4] == "O":
    if 7 in moves:
      choice = 7
  elif played[1] == "O" and played[7] == "O":
    if 4 in moves:
      choice = 4
  elif played[4] == "O" and played[7] == "O":
    if 1 in moves:
      choice = 1
  elif played[4] == "O" and played[5] == "O":
    if 6 in moves:
      choice = 6
  elif played[5] == "O" and played[6] == "O":
    if 4 in moves:
      choice = 4
  elif played[4] == "O" and played[6] == "O":
    if 5 in moves:
      choice = 5
  elif played[3] == "O" and played[5] == "O":
    if 7 in moves:
      choice = 7
  elif played[5] == "O" and played[7] == "O":
    if 3 in moves:
      choice = 3
  elif played[3] == "O" and played[5] == "O":
    if 7 in moves:
      choice = 7
  elif played[1] == "O" and played[5] == "O":
    if 9 in moves:
      choice = 9
  elif played[1] == "O" and played[9] == "O":
    if 5 in moves:
      choice = 5
  elif played[5] == "O" and played[9] == "O":
    if 1 in moves:
      choice = 1
  elif played[7] == "O" and played[8] == "O":
    if 9 in moves:
      choice = 9
  elif played[7] == "O" and played[9] == "O":
    if 8 in moves:
      choice = 8
  elif played[8] == "O" and played[9] == "O":
    if 7 in moves:
      choice = 7
  elif played[1] == "X" and played[2] == "X":
    if 3 in moves:
      choice = 3
  elif played[1] == "X" and played[3] == "X":
    if 2 in moves:
      choice = 2
  elif played[2] == "X" and played[3] == "X":
    if 1 in moves:
      choice = 1
  elif played[2] == "X" and played[5] == "X":
    if 8 in moves:
      choice = 8
  elif played[5] == "X" and played[8] == "X":
    if 2 in moves:
      choice = 2
  elif played[2] == "X" and played[8] == "X":
    if 5 in moves:
      choice = 5
  elif played[3] == "X" and played[6] == "X":
    if 5 in moves:
      choice = 5
  elif played[3] == "X" and played[5] == "X":
    if 6 in moves:
      choice = 6
  elif played[6] == "X" and played[5] == "X":
    if 3 in moves:
      choice = 3
  elif played[1] == "X" and played[4] == "X":
    if 7 in moves:
      choice = 7
  elif played[1] == "X" and played[7] == "X":
    if 4 in moves:
      choice = 4
  elif played[4] == "X" and played[7] == "X":
    if 1 in moves:
      choice = 1
  elif played[4] == "X" and played[5] == "X":
    if 6 in moves:
      choice = 6
  elif played[5] == "X" and played[6] == "X":
    if 4 in moves:
      choice = 4
  elif played[4] == "X" and played[6] == "X":
    if 5 in moves:
      choice = 5
  elif played[3] == "X" and played[5] == "X":
    if 7 in moves:
      choice = 7
  elif played[5] == "X" and played[7] == "X":
    if 3 in moves:
      choice = 3
  elif played[3] == "X" and played[5] == "X":
    if 7 in moves:
      choice = 7
  elif played[1] == "X" and played[5] == "X":
    if 9 in moves:
      choice = 9
  elif played[1] == "X" and played[9] == "X":
    if 5 in moves:
      choice = 5
  elif played[5] == "X" and played[9] == "X":
    if 1 in moves:
      choice = 1
  elif played[7] == "X" and played[8] == "X":
    if 9 in moves:
      choice = 9
  elif played[7] == "X" and played[9] == "X":
    if 8 in moves:
      choice = 8
  elif played[8] == "X" and played[9] == "X":
    if 7 in moves:
      choice = 7
  elif len(moves) <= 6:
    compPlay(played,moves,playedMoves)
  else:
    choice = random.choice(moves)
  print(choice)
  while choice not in moves:
    choice = random.choice(moves)
  moves.remove(choice)
  playedMoves.append(choice)
  print(moves,playedMoves,played)
  played[choice] = "O"
  if played[1] == "O" and played[2] == "O" and played[3] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[2] == "O" and played[5] == "O" and played[8] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[3] == "O" and played[6] == "O" and played[9] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[1] == "O" and played[4] == "O" and played[7] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[4] == "O" and played[5] == "O" and played[6] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[3] == "O" and played[5] == "O" and played[7] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[1] == "O" and played[5] == "O" and played[9] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()
  if played[7] == "O" and played[8] == "O" and played[9] == "O":
    print("Computer winswins!!!!!")
    drawBoard(played)
    sys.exit()


def gamePlayers():
  playerOne(played,moves,playedMoves)
  playerTwo(played,moves,playedMoves)
  playerOne(played,moves,playedMoves) 
  playerTwo(played,moves,playedMoves) 
  playerOne(played,moves,playedMoves) 
  playerTwo(played,moves,playedMoves) 
  playerOne(played,moves,playedMoves) 
  playerTwo(played,moves,playedMoves) 
  playerOne(played,moves,playedMoves) 
  drawBoard(played)
  print("StaleMate!!!!")

def gameVsComp():
  playerOne(played,moves,playedMoves)
  compPlay(played,moves,playedMoves)
  playerOne(played,moves,playedMoves)
  compPlay(played,moves,playedMoves)
  playerOne(played,moves,playedMoves)
  compPlay(played,moves,playedMoves)
  playerOne(played,moves,playedMoves)
  compPlay(played,moves,playedMoves)
  playerOne(played,moves,playedMoves)
  print("StaleMate!!!!")

def ruleBoard():
  print("\nCHoose a position")
  print("| 1 | 2 | 3 |")
  print("| 4 | 5 | 6 |")
  print("| 7 | 8 | 9 |")

def drawBoard(played):
  print("\nThese are all the remaining positions")
  print(f"| {played[1]} | {played[2]} | {played[3]} |")
  print(f"| {played[4]} | {played[5]} | {played[6]} |")
  print(f"| {played[7]} | {played[8]} | {played[9]} |")