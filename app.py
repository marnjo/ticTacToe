from tic_tac_toe import*

game = input("Single player ode or multiplayer mode? (S/M): ")

if game.upper() == "S":
  gameVsComp()
elif game.upper() == "M":
  gamePlayers()
else:
  print("Invalid choice")
