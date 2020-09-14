import pygame 
import random 
import time 
pygame.font.init() 
startTime = time.time() 

screen = pygame.display.set_mode( 
	(900, 650) 
) 
 
pygame.display.set_caption( 
	"SORTING VISUALISER"
) 

 
run = True

width = 900
length = 600
array = [0]*151
arr_clr = [(0, 204, 102)]*151
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0), 
	(0, 0, 153), (255, 102, 0)] 
fnt = pygame.font.SysFont("comicsans", 30) 
fnt1 = pygame.font.SysFont("comicsans", 20) 

def generate_arr(): 
for i in range(1, 151): 
arr_clr[i] = clr[0] 
array[i] = random.randrange(1, 100) 

 
generate_arr() 

def refill(): 
	screen.fill((255, 255, 255)) 
	draw() 
	pygame.display.update() 
	pygame.time.delay(10) 

 
def heapSort(array): 
	n = len(array) 
	for i in range(n//2-1, -1, -1): 
		pygame.event.pump() 
		heapify(array, i, n) 
	for i in range(n-1, 0, -1): 
		array[i], array[0] = array[0], array[i] 
		arr_clr[i] = clr[1] 
		refill() 
		heapify(array, 0, i) 


def heapify(array, root, size): 
	left = root * 2 + 1
	right = root * 2 + 2
	largest = root 
	if left < size and array[left] > array[largest]: 
		largest = left 
	if right < size and array[right] > array[largest]: 
		largest = right 
	if largest != root: 
		arr_clr[largest] = clr[2] 
		arr_clr[root] = clr[2] 
		array[largest],\ 
		array[root] = array[root],\ 
		array[largest] 
		refill() 
		arr_clr[largest] = clr[0] 
		arr_clr[root] = clr[0] 
		heapify(array, largest, size) 
		refill() 


def draw(): 

	# Text should be rendered 
	txt = fnt.render("SORT: PRESS 'ENTER'", 
					1, (0, 0, 0)) 
	# Position where text is placed 
	screen.blit(txt, (20, 20)) 
	txt1 = fnt.render("NEW ARRAY: PRESS 'R'", 
					1, (0, 0, 0)) 
	screen.blit(txt1, (20, 40)) 
	txt2 = fnt1.render("ALGORITHM USED:" +
					"HEAP SORT", 1, (0, 0, 0)) 
	screen.blit(txt2, (600, 60)) 
	text3 = fnt1.render("Running Time(sec): " +
						str(int(time.time() - startTime)), 
						1, (0, 0, 0)) 
	screen.blit(text3, (600, 20)) 
	element_width = (width-150)//150
	boundry_arr = 900 / 150
	boundry_grp = 550 / 100
	pygame.draw.line(screen, (0, 0, 0), (0, 95), 
					(900, 95), 6) 

	 
	for i in range(1, 151): 
		pygame.draw.line(screen, arr_clr[i], 
						(boundry_arr * i-3, 100), 
						(boundry_arr * i-3, 
						array[i]*boundry_grp + 100),\ 
						element_width) 


 
while run: 
	# background 
	screen.fill((255, 255, 255)) 

	
	for event in pygame.event.get(): 

		# If we click Close button in window 
		if event.type == pygame.QUIT: 
			run = False
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_r: 
				generate_arr() 
			if event.key == pygame.K_RETURN: 
				heapSort(array) 
	draw() 
	pygame.display.update() 

pygame.quit() 

 
