
import pygame

from constants import *
from termcolor import colored


BSIZ = int(input("\033[1;4mSelect BSIZ:\033[0m "))
while BSIZ < 3:
	print("BSIZ should be at least 3.")
	BSIZ = int(input("\033[1;4mSelect BSIZ:\033[0m "))
	
ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))
while ST_PLAYER < 3 or ST_PLAYER > (BSIZ**2 - 1)//2:
	if ST_PLAYER < 3:
		print("The amount of stones should be at least 3.")
		ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))
	elif ST_PLAYER > (BSIZ**2 - 1)//2:
		print("Invalid amount of stones.")
		ST_PLAYER = int(input("\033[1;4mSelect the amount of stones:\033[0m "))

print("\n\033[1;4mChoose mode:\033[0m")
MODE = int(input("\033[1mClassic mode(0)\nInverse mode(1)\n\033[0m"))
while MODE > 1 or MODE < 0:
	print("Invalid mode.")
	MODE = int(input("\033[1;4mChoose mode:\nClassic mode(0)\nInverse mode(1)\n\033[0m"))

PLY1 = str(input("\n\033[1mName player1:\033[0m "))
PLY2 = str(input("\033[1mName player2:\033[0m "))

PLY1_C = str('blue')
PLY2_C = str('red')

if MODE == 0:
	print("To win this game you have to make three in a row.")
elif MODE == 1:
	print("To win this game you have to avoid making three in a row.")
input("\n\033[1mpress <enter> to start playing.\033[0m")

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Three in a row")
clock = pygame.time.Clock()

from abs_board_h import set_board_up

stones, select_st, move_st, draw_txt, win, contador, turno = set_board_up(BSIZ,ST_PLAYER,MODE,PLY1,PLY2,PLY1_C,PLY2_C)

def trans_coord(x, y):
	'translates pixel coordinates into board coordinates'
	return round((x - ROOM - SEP - 0.5*SLOT)/(SEP + SLOT)), round((y - SEP - 0.5*SLOT)/(SEP + SLOT))

def draw_square(screen, i, j):
    pygame.draw.polygon(screen, GRAY,
		( (ROOM + SEP + i*(SLOT + SEP), SEP + j*(SLOT + SEP)),
			(ROOM + SEP + i*(SLOT + SEP) + SLOT, SEP + j*(SLOT + SEP)),
			(ROOM + SEP + i*(SLOT + SEP) + SLOT, SEP + j*(SLOT + SEP) + SLOT),
			(ROOM + SEP + i*(SLOT + SEP), SEP + j*(SLOT + SEP) + SLOT)
		))

def draw_stone(screen, i, j, color):
	pygame.draw.circle(screen, color, 
		(ROOM + 0.5*SEP + (i + 0.5)*(SLOT + SEP), 0.5*SEP + (j + 0.5)*(SLOT + SEP)), 
		RAD)

def draw_board(curr_player = 0, end = False):
	'on fresh screen, draw grid, stones, player turn mark, then make it appear'
	screen.fill(WHITE if not end else GRAY)
	for i in range(BSIZ):
		for j in range(BSIZ):
			draw_square(screen, i, j)
	for s in stones():
		draw_stone(screen, *s)
	if not end:
		'colored rectangle indicates who plays next'
		pygame.draw.rect(screen, PLAYER_COLOR[curr_player], 
		(ROOM + SEP, BSIZ*(SEP + SLOT) + SEP, BSIZ*(SEP + SLOT) - SEP, SLOT)
		)
	pygame.display.flip()


stone_selected = True
curr_player = 0

draw_board()

done = False


end = False

while not done:
    
	clock.tick(10)
    
	for event in pygame.event.get(): 
		"User did something"
		if event.type == pygame.QUIT:
			"User clicked 'close window', set flag to exit loop"
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN and not end:
			"game is afoot and user clicked something"
			if stone_selected:
				"User should click on a free destination square, otherwise ignore event"
				stone_selected, curr_player, end = move_st(*trans_coord(*event.pos))
				draw_board(curr_player, end)
			else:
				"User should click on a stone to select it"
				stone_selected = select_st(*trans_coord(*event.pos))

# Friendly finish-up:
print('Game over')
win()

pygame.quit()
