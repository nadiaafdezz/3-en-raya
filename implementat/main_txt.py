
from abs_board_h import set_board_up
import time
from random import randrange
from termcolor import colored

# choose the board size
BSIZ = int(input("\033[1;4mSelect BSIZ:\033[0m "))
while BSIZ < 3:
	print("BSIZ should be at least 3.")
	BSIZ = int(input("\033[1;4mSelect BSIZ:\033[0m "))
	
# choose the stones/player
ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))
while ST_PLAYER < 3 or ST_PLAYER > (BSIZ**2 - 1)//2:
	if ST_PLAYER < 3:
		print("The amount of stones should be at least 3.")
		ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))
	elif ST_PLAYER > (BSIZ**2 - 1)//2:
		print("Invalid amount of stones.")
		ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))

# choose the mode
print("\n\033[1;4mChoose mode:\033[0m")
MODE = int(input("\033[1mClassic mode(0)\n\033[1mInverse mode(1)\n\033[0m"))
while MODE > 1 or MODE < 0:
	print("Invalid mode.")
	MODE = int(input("\033[1;4mChoose mode:\nClassic mode(0)\nInverse mode(1)\n\033[0m"))

# choose the difficulty
print("\n\033[1;4mChoose difficulty:\033[0m")
DIF = int(input("\033[1mSum mode(0)\nMultiplication mode(1)\n\033[0m"))
while DIF > 1 or DIF < 0:
	print("Invalid mode.")
	DIF = int(input("\033[1;4mChoose difficulty:\nSum mode(0)\nMultiplication mode(1)\n\033[0m"))

# conf your player
PLY1 = str(input("\n\033[1mName player1:\033[0m "))
print("\033[1;4mChoose your colour:\033[0m")
PLY1_C = str(input("\033[1mred,green,yellow,blue,magenta,cyan\n\033[0m"))
while PLY1_C != 'red' and PLY1_C != 'green' and PLY1_C != 'yellow' and PLY1_C != 'blue' and PLY1_C != 'magenta' and PLY1_C != 'cyan':
	print("Invalid colour.")
	PLY1_C = str(input("\033[1mred,green,yellow,blue,magenta,cyan\n\033[0m"))

PLY2 = str(input("\n\033[1mName player2:\033[0m "))
print("\033[1;4mChoose your colour:\033[0m")
PLY2_C = str(input("\033[1mred,green,yellow,blue,magenta,cyan\n\033[0m"))
while PLY2_C != 'red' and PLY2_C != 'green' and PLY2_C != 'yellow' and PLY2_C != 'blue' and PLY2_C != 'magenta' and PLY2_C != 'cyan' or PLY2_C== PLY1_C:
	if PLY2_C== PLY1_C:
		print("The colour you have chosen is already used for player1.")
		PLY2_C = str(input("\033[1mred,green,yellow,blue,magenta,cyan\n\033[0m"))
	else: 
		print("Invalid colour.")
		PLY2_C = str(input("\033[1mred,green,yellow,blue,magenta,cyan\n\033[0m"))
		
print('\n',colored(PLY1,PLY1_C),"\033[1myou are\033[0m", colored("\033[1mX\033[0m", PLY1_C),'\n',colored(PLY2,PLY2_C),"\033[1myou are\033[0m", colored("\033[1mO\033[0m", PLY2_C))

# explanation of your game configuration
if MODE == 0 and DIF == 0:
	print("\n To win this game you have to make three in a row, but before you roll, you must respond correctly to a sum, if you don't answer well you will lose your turn.")
elif MODE == 1 and DIF == 0:
	print("\n To win this game you have to avoid making three in a row, but before rolling, you must answer correctly to a sum, if you don't answer correctly you will lose your turn.")
elif MODE == 1 and DIF == 1:
	print("\n To win this game you have to avoid making three in a row, but before rolling, you must answer correctly to a multiplication, if you don't answer correctly you will lose your turn.")
elif MODE == 0 and DIF == 1:
	print("\n To win this game you have to make three in a row, but before you roll, you must respond correctly to a multiplication, if you don't answer well you will lose your turn.")
input("\n\033[1mpress <enter> to start playing.\033[0m")



stones, select_st, move_st, draw_txt, win, contador, turno = set_board_up(BSIZ,ST_PLAYER,MODE,PLY1,PLY2,PLY1_C,PLY2_C)
stone_selected = True

end = False
draw_txt(False)

while not end:
	
	while not stone_selected:
		print(PLY2 if turno()==1 else PLY1,end=", ")
		i, j = input("\033[1mselect stone coordinates: \033[0m").split()
		stone_selected = select_st(int(i), int(j))
		draw_txt(end)
	while stone_selected and not end:
		
		print("\033[1mIt's the turn of\033[0m",(colored(PLY2, PLY2_C) if turno()==1 else colored(PLY1, PLY1_C)))
		if DIF==0:
			x = randrange(0,100)
			y = randrange(0,100)
			print(x,'+',y,end=" ")
			res = int(input('= '))
		else:
			x = randrange(0,31)
			y = randrange(0,31)
			print(x,'x',y,end=" ")
			res = int(input('= '))
		
		if (DIF==0 and res == x+y) or (DIF==1 and res ==x*y):
			i, j = input("\033[1mSelect destination coordinates: \033[0m").split()
			stone_selected, curr_player, end = move_st(int(i), int(j))
			draw_txt(end)
		else:
			print("\nYou have lost your turn, the correct answer is", (x+y if DIF==0 else x*y))
			input("\033[1mpress <enter> to continue.\033[0m\n")
			stone_selected=contador()
		

time.sleep(0.5)
print("\033[1mGame over.\033[0m")
win()
