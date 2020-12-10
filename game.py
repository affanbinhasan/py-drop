import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)                                                                                                                          
BLUE = (0,0,255)
SPEED = 0
SCORE = 0

player_size = 50
player_pos = [WIDTH/2,HEIGHT-2*player_size]

BACKGROUND_COLOR = (0,254,0)

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace" , 35 )

def set_level(SCORE,SPEED):
#	if SCORE < 20:
#		SPEED = 5
#	elif SCORE < 40:
#		SPEED = 8
#	elif SCORE < 60:
#		SPEED = 10
#	else:
#		SPEED = 15
	SPEED = SCORE/5 + 5
	return SPEED



def drop_enemy(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1 :
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos,y_pos])

def draw_enemy(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def update_enemy_positions(enemy_list, SCORE):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			SCORE += 1

	return SCORE
	
def collision_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos,player_pos):
			return True
	return False

def detect_collision(player_pos,enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True 
		return False	

while not game_over:

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size

			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)

	#if detect_collision(player_pos,enemy_pos):
	#	game_over = True
	#	break

	drop_enemy(enemy_list)
	SCORE = update_enemy_positions(enemy_list,SCORE)
	SPEED = set_level(SCORE,SPEED)

	text = "Score" + " : " + str(SCORE)
	label = myFont.render(text,1, BLACK)
	screen.blit(label, (WIDTH-250,HEIGHT-40))

	
	if collision_check(enemy_list,player_pos):
		game_over = True
		break

	draw_enemy(enemy_list)



	pygame.draw.rect(screen, RED,(player_pos[0],player_pos[1],player_size,player_size))

	

	clock.tick(30)



	pygame.display.update()

print("YOUR FINAL SCORE IS " + ":" + str(SCORE))

