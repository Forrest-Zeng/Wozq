dimensions=15
board=[[0 for _ in range(dimensions)] for _ in range(dimensions)]
 
def add_piece(x,y,side):
 if board[y][x] == 0:
   board[y][x] = side
   return True
 else:
   return False
 
def check_win(side):
 for i in range(dimensions):
   for j in range(dimensions):
     # could do this recursively but lazyness
     if board[i][j] == side:
       for k in range(-1,2):
         for l in range(-1,2):
           if 0 <= i+k < dimensions and 0 <= j+l < dimensions and not (k==0 and l==0):
             if board[i+k][j+l] == side:
               count=0
               while board[i+count*k][j+count*l] == side:
                 count+=1
               if count >= 5:
                 return True
 return False
 
 
'''
you can customize but im saying black is 1
and white is 2
'''
 
# add_piece(0,0,1)
# add_piece(1,1,1)
# add_piece(2,2,1)
# add_piece(3,3,1)
# add_piece(4,4,1)
# add_piece(5,5,1)
# print(check_win(1))
