"""
Aleksei Rovenich
29/9/2020
Conway's Game of Life
"""
from tkinter import *
from time import sleep
import random
def escenario(canvas, width, height):
	canvas.delete("all")
	for i in range(0, width, 10):
		canvas.create_line(i, 0, i, height, fill="#000000" )

	for j in range(0, height, 10):
		canvas.create_line(0, j, width, j, fill="#000000")

def celula(width, height):
	cell = []
	aux = []
	for i in range(width//10):
		for j in range(height//10):
			aux.append(random.randint(0,1))
		cell.append(aux)
		
		aux = []
	

	return cell


def printCell(canvas, cell):
	for i in range(len(cell)):
		for j in range(len(cell)):

			if cell[i][j] == 1:
				canvas.create_rectangle(i * 10, j * 10, (i * 10) + 10, (j * 10) + 10, fill="#ffffff")
			else:
				canvas.create_rectangle(i * 10, j * 10, (i * 10) + 10, (j * 10) + 10, fill="#000000")


def moveCell(cell, width, height):
	
	state = list(cell)
	
	for i in range(-1, len(cell) - 1, 1):
		for j in range(-1, len(cell) - 1, 1):
			state[j][i] = newCell(cell, i, j)

	cell = list(state)

	return cell


def newCell(cell, x, y):
	
	state = cell[x][y]
	vecinos = 0
	for i in range(x - 1, x + 2, 1):
		for j in range(y - 1, y + 2, 1):
			
			vecinos += cell[i][j]
			
	vecinos -= cell[x][y]
	
	if state == 0 and vecinos == 3:
		
		return 1
	elif state == 1 and (vecinos < 2 or vecinos > 3):
		
		return 0
	else:
		
		return state


def main(canvas, width, height):

	#setup/start
	cell = celula(width, height)
	printCell(canvas, cell)
	cell = moveCell(cell, width, height)

	#update
	while 1:
		
		escenario(canvas, width, height)
		cell = moveCell(list(cell), width, height)
		printCell(canvas, cell)
		#mainloop() #si se usa esto, no se ejecuta el codigo de abajo
		#usaremos lo de a continuacion para hacer un loop
		master.update_idletasks()
		master.update()
		sleep(0.1)

###########################################################################################################################
if __name__ == "__main__":
	master = Tk()
	res = 300
	canvas_width = res
	canvas_height = res
	
	w = Canvas(master, width=canvas_width, height=canvas_height)
	w.pack()

	main(w, canvas_width, canvas_height)
