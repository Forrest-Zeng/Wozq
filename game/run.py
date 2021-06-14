import game
import random
 
def start():
 winner = None
 current=1
 while not winner:
   print("Player ",current,"'s turn.")
   while True:
     try:
       move=input("Input coordinates like this, x y: ")
       x_coord=int(move.split(" ")[0])
       y_coord=int(move.split(" ")[1])
       added=game.add_piece(x_coord,y_coord,current)
       if not added:
         raise(AttributeError)
     except AttributeError:
       print("There's already a piece there.")
       continue
     except ValueError:
       print("Looks like you typed it wrong.")
       continue
     except IndexError:
       print("Looks like you typed it wrong. It has to be in the dimensions, from 0 to", game.dimensions-1,".")
       continue
     break
    
 
   for row in game.board:
     print(row)
   if game.check_win(current):
     print("Player", current, "wins!")
     break
   current=2 if current == 1 else 1
 
 
 

