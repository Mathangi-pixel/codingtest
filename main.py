

import string
import random
import sys
game_on = True
move = 0
list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(list1)
print('\n'*2)
matrix=[]
while list1 !=[]:
    matrix.append(list1[:4])
    list1 = list1[4:]



def zero(board):
   global empty_space
   for x in range (len(board)):
       for y in range(len(board[x])):
           if board[x][y] == 0:
               empty_space = (x,y)

   return empty_space






def draw_board(board):
    print('\n\t+-------+-------+-------+-------|')

    for x in range (len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:

                print('\t|  0' , end='')
            else:
                 print('\t|  ' + '{:02d}' .format(board[x][y]), end=' ')

        print('\n\t+-------+-------+-------+-------|')




def ask_number():
    global num , piece
    num = input('\nplease type the number of the piece to move :   ')


    num = int(num)
    piece=()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)
    return piece , num





zero(matrix)

while game_on:
    draw_board(matrix)

    ask_number()
    if num > 15:
        print('illegal move , try again  ')
    else:

        if(empty_space==(piece[0]-1,piece[1]))\
           or(empty_space==(piece[0]+1,piece[1]))\
           or(empty_space==(piece[0],piece[1]-1))\
           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=num
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print()
            print('you have made ',move , 'moves so far ')
            print(2*'\n')
        else:
            print('illegal move , try again ')
