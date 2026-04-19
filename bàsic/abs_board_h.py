# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(ST_PLAYER = 4):
	tablero=['  ']*BSIZ**2
	cont=0	
	m=0
	def stones():
		tab=[]
		for i in range (0,len(tablero)):
					
			if tablero[i]=='X ':
				color = PLAYER_COLOR[0]
			elif tablero[i]=='O ':
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
		nonlocal m, cont
		m=i*BSIZ+j
		if 0<= i < BSIZ and 0<= j < BSIZ:	
			if (cont%2==0 and tablero[m]=='X ') or (cont%2!=0 and tablero[m]=='O '):
				return True
			else:
				print("This square hasn't got any of your stones")
		else:
			print('This square is out of board')
			

	def end():
		fila = 0
		columna = 0
		diagonal1 = 0
		diagonal2 = 0
		while fila<BSIZ**2-2:
			while (fila+2)%BSIZ!=0:
				if tablero[fila]==tablero[fila+1]==tablero[fila+2]==('X ') or tablero[fila]==tablero[fila+1]==tablero[fila+2]==('O '):
					return True
				fila+=1
			fila+=2
			
		while columna<BSIZ*(BSIZ-2):
			if tablero[columna]==tablero[columna+BSIZ]==tablero[columna+BSIZ*2]==('X ') or tablero[columna]==tablero[columna+BSIZ]==tablero[columna+BSIZ*2]==('O '):
				return True
			columna+=1
		
		while diagonal1 <= BSIZ*(BSIZ-3)+BSIZ-3:
			while (diagonal1 + 2*BSIZ + 2)%BSIZ!= 0:
				if tablero[diagonal1]==tablero[BSIZ+1+diagonal1]==tablero[2*BSIZ+2+diagonal1]==('X ') or tablero[diagonal1]==tablero[BSIZ+1+diagonal1]==tablero[2*BSIZ+2+diagonal1]==('O '):
					return True
				diagonal1 += 1
			diagonal1 += 2
				
		while diagonal2 < BSIZ*(BSIZ-2):		
			while diagonal2%BSIZ!= 0:
				if tablero[diagonal2]==tablero[diagonal2 +BSIZ -1]==tablero[diagonal2 + 2*BSIZ -2]==('X ') or tablero[diagonal2]==tablero[diagonal2 +BSIZ -1]==tablero[diagonal2 + 2*BSIZ -2]==('O '):
					return True		
				diagonal2 += 1
			diagonal2 += 2				

		return False

	def move_st(i, j):
		k=i*BSIZ+j
		nonlocal m, cont
		g=False
		f=False
		if 0<= i < BSIZ and 0<= j < BSIZ:			
			if tablero[k]=='  ':
				tablero[k]='X ' if cont%2==0 else 'O '
				cont+=1
				if cont-1>=ST_PLAYER*2:
					tablero[m]='  '	
			else:
				print('This square is occupied')
				g = True	
		else:
			print('This square is out of board')
			f = True					

		return (cont//2<ST_PLAYER or f or g), 0 if cont%2==0 else 1 , end()
		
		
	def draw_txt(end=False):
		print("","-"*(6*BSIZ-1))
		for fila in range(0,BSIZ):
			print("|", end="")
			for columna in range(0,BSIZ):
				x = fila*BSIZ + columna
				print(" ", tablero[x], "|", end="")
			print("\n","-"*(6*BSIZ-1))
				
	return stones, select_st, move_st, draw_txt
