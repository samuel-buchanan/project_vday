import pygame
#commands = ["quit", "exit", "look"]

def first_room(self):
	if "fight" in self:
		success = ["You fight the bear and win!", "After victoriously fighting the bear, you walk into the kitchen.", "Blocking your way you see a sphinx. He is itching to talk to you.", "The door to the pantry is ajar."]
		return(success)
	elif "beat up" in self:
		success = ["You fight the bear and win!", "After victoriously fighting the bear, you walk into the kitchen.", "Blocking your way you see a sphinx. He is itching to talk to you.", "The door to the pantry is ajar."]
		return(success)
	elif "look" in self:
		description = ["The front room seems normal. Toys on the floor, couch, TV.", "The bear, however, seems out of place. You think you could beat him up."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)

def second_room(self):
	if "mirror" in self or "reflection" in self:
		success = ["After answering correctly, the sphinx fades from existance.", "Behind him was a vase of flowers!", "You make your way to the dining room after solving the riddle of the sphinx.", "You see a small but vicious honey badger.", "She is sitting on and guarding a brightly wrapped Valentine's Day present.", "You notice an oblong, light pink machine with a tangled white cord.", "It is on top of some thick, colorful card stock."]
		return(success)
	elif "look" in self and "kitchen" in self:
		description = ["The under-cabinet lighting really accentuates the place.", "You wish the countertops were cleaner."]
		return(description)
	elif "look" in self and "pantry" in self:
		description = ["The sphinx makes no move to stop you.", "You notice that someone has eaten most of the Happy Hippos."]
		return(description)
	elif "look" in self and "sphinx" in self:
		description = ["Ancient and mysterious, sphinxes are known for their riddling ability.", "He looks like he wants to ask you something."]
		return(description)
	elif "talk" in self:
		description = ["He asks you a riddle:", "I look at you, you look at me. You raise your right, I raise my left.", "What am I?", "What is your answer?"]
		return(description)
	elif "look" in self:
		description = ["Please specify what you'd like to look at."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)

def third_room(self):
	if "use" in self and "Cricut" in self:
		description = ["You use the cardstock and Cricut to produce a lovely little card.", "You give the card to the badger.", "She calms down and returns to playing with the horses in the stable.", "You get the package.", "You win the game!"]
		return(description)
	elif "use" in self and "cricut" in self:
		description = ["You use the cardstock and Cricut to produce a lovely little card.", "You give the card to the badger.", "She calms down and returns to playing with the horses in the stable.", "You get the package.", "You win the game!"]
		return(description)
	elif "look" in self and "badger" in self:
		description = ["Badgers can usually be distracted by shiny or colorful things.", "Maybe even well-designed and colorful things (hint, hint!)"]
		return(description)
	elif "look" in self and "machine" in self:
		description = ["It is rose-tinted and has various buttons and dials on the top.", "Different-colored markers jut out of a holder on one end.", "It says Cricut on the top."]
		return(description)
	elif "look" in self and "cricut" in self:
		description = ["It is rose-tinted and has various buttons and dials on the top.", "Different-colored markers jut out of a holder on one end.", "It says Cricut on the top."]
		return(description)
	elif "look" in self and "Cricut" in self:
		description = ["It is rose-tinted and has various buttons and dials on the top.", "Different-colored markers jut out of a holder on one end.", "It says Cricut on the top."]
		return(description)
	elif "look" in self:
		description = ["Please specify what you'd like to look at."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)
