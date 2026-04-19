
from constants import PLAYER_COLOR, NO_PLAYER, GRAY, ST_PLAYER
from collections import namedtuple
from termcolor import colored

Stone = namedtuple('Stone', ('x', 'y', 'color'))

def set_board_up(BSIZ, ST_PLAYER, MODE, PLY1, PLY2, PLY1_C, PLY2_C):
	
	tablero=['  ']*(BSIZ**2)
	cont = 0
	m=0
	tiradas_p1 = 0
	tiradas_p2 = 0
	player1 = colored("X ", PLY1_C)
	player2 = colored("O ",PLY2_C)
	tur=0
	
	def contador():
		nonlocal tur
		tur = 1- tur
		p = False
		if tur == 0:
			if tiradas_p1 < ST_PLAYER:
				p = True
		else:
			if tiradas_p2 < ST_PLAYER:
				p = True
		return p
	
	
	def turno():
		return tur
	

	def stones():
		tab=[]
		for i in range (0,len(tablero)):
					
			if tablero[i]==player1:
				color = PLAYER_COLOR[0]
			elif tablero[i]==player2:
				color = PLAYER_COLOR[1]
			else:
				color = GRAY
			j=0
			
			while j<len(tablero):
				if j<=i<j+BSIZ:
					tab += [(i//BSIZ,i-j,color)]
				j += BSIZ		
		
		
		return tab



	def select_st(i, j):
		nonlocal m, cont, tur
		m=i*BSIZ+j
		if 0 <= i < BSIZ and 0 <= j <BSIZ:	
			if (tur==0 and tablero[m]== player1) or (tur==1 and tablero[m]==player2):
				return True
			else:
				print("This square hasn't got any of your stones, try again.")
		else:
			print('This square is out of board, try again.')



	def end():
		fila = 0
		columna = 0
		diagonal1 = 0
		diagonal2 = 0
		while fila<BSIZ**2-2:
			while (fila+2)%BSIZ!=0:
				if tablero[fila]==tablero[fila+1]==tablero[fila+2]==(player1) or tablero[fila]==tablero[fila+1]==tablero[fila+2]==(player2):
					return True
				fila+=1
			fila+=2
			
		while columna<BSIZ*(BSIZ-2):
			if tablero[columna]==tablero[columna+BSIZ]==tablero[columna+BSIZ*2]==(player1) or tablero[columna]==tablero[columna+BSIZ]==tablero[columna+BSIZ*2]==(player2):
				return True
			columna+=1
		
		while diagonal1 <= BSIZ*(BSIZ-3)+BSIZ-3:
			while (diagonal1 + 2*BSIZ + 2)%BSIZ!= 0:
				if tablero[diagonal1]==tablero[BSIZ+1+diagonal1]==tablero[2*BSIZ+2+diagonal1]==(player1) or tablero[diagonal1]==tablero[BSIZ+1+diagonal1]==tablero[2*BSIZ+2+diagonal1]==(player2):
					return True
				diagonal1 += 1
			diagonal1 += 2
				
		while diagonal2 < BSIZ*(BSIZ-2):		
			while diagonal2%BSIZ!= 0:
				if tablero[diagonal2]==tablero[diagonal2 +BSIZ -1]==tablero[diagonal2 + 2*BSIZ -2]==(player1) or tablero[diagonal2]==tablero[diagonal2 + BSIZ -1]==tablero[diagonal2 + 2*BSIZ -2]==(player2):
					return True		
				diagonal2 += 1
			diagonal2 += 2	

		return False



	def move_st(i, j):
		nonlocal m, cont, tiradas_p1, tiradas_p2, tur
		g = False
		f = False
		k=i*BSIZ+j
		if 0<= i < BSIZ and 0<= j < BSIZ:		
			if tablero[k]=='  ':
				if tur == 0:
					tablero[k] = player1
					tiradas_p1 += 1
				else: 
					tablero[k] = player2
					tiradas_p2 += 1
				tur = 1- tur
				if tur == 0:
					if tiradas_p2 > ST_PLAYER:
						tablero[m]='  '
				else:
					if tiradas_p1 > ST_PLAYER:
						tablero[m]='  '
			else:
				print('This square is occupied, try again.')
				g = True
		else:
			 print('This square is out of board, try again.')
			 f = True
			 
		p = False
		if tur == 0:
			if tiradas_p1 < ST_PLAYER:
				p = True
		else:
			if tiradas_p2 < ST_PLAYER:
				p = True
		return (p or f or g),tur, end()
		
		
		
	def draw_txt(end=False):
		print("","-"*(6*BSIZ-1))
		for fila in range(0,BSIZ):
			print("|", end="")
			for columna in range(0,BSIZ):
				x = fila*BSIZ + columna
				print(" ", tablero[x], "|", end="")
			print("\n","-"*(6*BSIZ-1))

			
	def win():
		nonlocal tur
		if MODE == 0:
			print('',colored(PLY1, PLY1_C) if turno() == 1 else colored(PLY2, PLY2_C), 'won!\n', colored(PLY2, PLY2_C) if turno() == 1 else colored(PLY1, PLY1_C),"next time be more aware, don't give up!")
		else:
			print('',colored(PLY1, PLY1_C) if turno() == 0 else colored(PLY2, PLY2_C), 'won!\n', colored(PLY2, PLY2_C) if turno() == 0 else colored(PLY1, PLY1_C),"next time be more aware, don't give up!")

			
			
	return stones, select_st, move_st, draw_txt, win, contador, turno
	

