import pygame
#import input_handler
from game_rooms import first_room, second_room, third_room

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
done = False
splash_screen_over = False
win_screen_over = False

font = pygame.font.SysFont(None, 48)
parser_font = pygame.font.SysFont(None, 72)

bear_pelt = pygame.image.load("bearpelt16x16.bmp")
startup_splash = pygame.image.load("AsVdayAdventure.bmp")
you_win = pygame.image.load("you_win_yellow.bmp")

pygame.display.set_caption("*Amanda's Valentine's Day Adventure*")

text1_string = ""
text2_string = ""
text3_string = ""
text4_string = ""
text5_string = ""
text6_string = "Samsoft Presents:"
text7_string = "*Amanda's Valentine's Day Adventure*"
text8_string = ""
text9_string = "Type 'quit' or 'exit' to close the program."
text10_string = "Type 'look' to see a little description of where you are."
text11_string = ""
text12_string = ""
text13_string = "You walk in the front door of the house."
text14_string = "Instead of someone on their laptop on the couch, you instead see a bear."
input_string = ""

text_string_list = [text1_string, text2_string, text3_string, text4_string, text5_string, text6_string, text7_string, text8_string, text9_string, text10_string, text11_string, text12_string, text13_string, text14_string]

inventory = []

text1 = font.render(text1_string, True, (65, 0, 0))
text2 = font.render(text2_string, True, (65, 0, 0))
text3 = font.render(text3_string, True, (65, 0, 0))
text4 = font.render(text4_string, True, (90, 0, 0))
text5 = font.render(text5_string, True, (90, 0, 0))
text6 = font.render(text6_string, True, (125, 0, 0))
text7 = font.render(text7_string, True, (125, 0, 0))
text8 = font.render(text8_string, True, (125, 0, 0))
text9 = font.render(text9_string, True, (125, 0, 0))
text10 = font.render(text10_string, True, (125, 0, 0))
text11 = font.render(text11_string, True, (125, 0, 0))
text12 = font.render(text12_string, True, (125, 0, 0))
text13 = font.render(text13_string, True, (125, 0, 0))
text14 = font.render(text14_string, True, (125, 0, 0))
text15 = parser_font.render(f">{input_string}", True, (255, 0, 0))


def render_all_lines():
	screen.blit(text1, (0, 0))
	screen.blit(text2, (0, 35))
	screen.blit(text3, (0, 70))
	screen.blit(text4, (0, 105))
	screen.blit(text5, (0, 140))
	screen.blit(text6, (0, 175))
	screen.blit(text7, (0, 210))
	screen.blit(text8, (0, 245))
	screen.blit(text9, (0, 280))
	screen.blit(text10, (0, 315))
	screen.blit(text11, (0, 350))
	screen.blit(text12, (0, 385))
	screen.blit(text13, (0, 420))
	screen.blit(text14, (0, 455))
	screen.blit(text15, (0, 510))

def render_inventory(inventory):
	if "bear pelt" in inventory:
		screen.blit(bear_pelt, (1100, 25))
	# follow up with rest of inventory here


# Start screen code below
while not splash_screen_over:
	for event in pygame.event.get():
		screen.fill((255, 255, 0))
		splash_text = font.render("Welcome to your adventure!", True, (0, 0, 0))
		screen.blit(startup_splash, (60, 86))
		press_enter_text = font.render("Press enter to start.", True, (0, 0, 0))
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			splash_screen_over = True
		screen.blit(splash_text, (0,225))
		screen.blit(press_enter_text, (0, 300))
		pygame.display.update()


while not done:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done = True
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
			input_string = input_string[:-1]
			text15 = parser_font.render(f">{input_string}", True, (255, 0, 0))
		elif event.type == pygame.KEYDOWN:
			if event.unicode.isalnum() == True or event.key == pygame.K_SPACE:
				input_string = input_string + event.unicode
				text15 = parser_font.render(f">{input_string}", True, (255, 0, 0))
				screen.blit(text15, (0, 510))
				pygame.display.update()

		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			if "quit" in input_string or "exit" in input_string:
				done = True
				break


			# MAIN GAME ROOM LOOP HERE
			text_string_list.append(">" + input_string)
			
			if "bear pelt" in inventory and "tentacle" in inventory:
				room_output = third_room(input_string)
				for i in range(0, len(room_output)):
					text_string_list.append(room_output[i])
				if "You win the game!" in room_output:
					inventory.append("stoat skin")

			elif "bear pelt" in inventory:
				room_output = second_room(input_string)
				for i in range(0, len(room_output)):
					text_string_list.append(room_output[i])
				if "It is on top of some thick, colorful card stock." in room_output:
					inventory.append("tentacle")

			else:
				room_output = first_room(input_string)
				if "The door to the pantry is ajar." in room_output:
					inventory.append("bear pelt")
				for i in range(0, len(room_output)):
					text_string_list.append(room_output[i])


			text1_string = text_string_list[-14]
			text2_string = text_string_list[-13]
			text3_string = text_string_list[-12]
			text4_string = text_string_list[-11]
			text5_string = text_string_list[-10]
			text6_string = text_string_list[-9]
			text7_string = text_string_list[-8]
			text8_string = text_string_list[-7]
			text9_string = text_string_list[-6]
			text10_string = text_string_list[-5]
			text11_string = text_string_list[-4]
			text12_string = text_string_list[-3]
			text13_string = text_string_list[-2]
			text14_string = text_string_list[-1]
			
			input_string = ""
			
			text1 = font.render(text1_string, True, (65, 0, 0))
			text2 = font.render(text2_string, True, (65, 0, 0))
			text3 = font.render(text3_string, True, (65, 0, 0))
			text4 = font.render(text4_string, True, (90, 0, 0))
			text5 = font.render(text5_string, True, (90, 0, 0))
			text6 = font.render(text6_string, True, (90, 0, 0))
			text7 = font.render(text7_string, True, (90, 0, 0))
			text8 = font.render(text8_string, True, (125, 0, 0))
			text9 = font.render(text9_string, True, (125, 0, 0))
			text10 = font.render(text10_string, True, (125, 0, 0))
			text11 = font.render(text11_string, True, (125, 0, 0))
			text12 = font.render(text12_string, True, (125, 0, 0))
			text13 = font.render(text13_string, True, (125, 0, 0))
			text14 = font.render(text14_string, True, (125, 0, 0))
			text15 = parser_font.render(f">{input_string}", True, (255, 0, 0))

		#elif event.type == pygame.K_END:
			#cursor_position = len(input_string)
		#elif event.type == pygame.K_HOME:
			#cursor_position = 0

		
	screen.fill((0, 0, 0))
	render_all_lines()
	render_inventory(inventory)
	pygame.display.update()
	clock.tick(30)
	
	# win screen
	if "bear pelt" in inventory and "tentacle" in inventory and "stoat skin" in inventory:
		pygame.time.wait(5000)
		while not win_screen_over:
			for event in pygame.event.get():
				screen.fill((0, 0, 255))
				winscreen_text = font.render("You have won your adventure!", True, (0, 0, 0))
				win_enter_text = font.render("Press enter to close the program.", True, (0, 0, 0))
				if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					win_screen_over = True
					done = True
					break
				screen.blit(you_win, (284, 9))
				screen.blit(winscreen_text, (0, 225))
				screen.blit(win_enter_text, (0, 300))
				pygame.display.update()
