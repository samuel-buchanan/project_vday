import pygame
#commands = ["quit", "exit", "look"]

def first_room(self):
	if "fight" in self:
		success = ["You fight the bear.", "But eventually you triumph. You get a bear pelt.", "You move along to the next room and see a gigantic red octopus guarding the exit. Weird."]
		return(success)
	elif "look" in self:
		description = ["The room is pretty normal, TV, toys on the floor, etc.", "The bear is quite large, though."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)

def second_room(self):
	if "fight" in self:
		success = ["You fight the octopus valiantly.", "You chop off one of his tentacles and he retreats.", "You move along to the next room and see a weirdly large weasel in front of something shiny."]
		return(success)
	elif "look" in self:
		description = ["You're not sure how an octopus got in the house, but he's definitely here now."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)

def third_room(self):
	if "fight" in self:
		success = ["You fight the giant weasel. He was guarding a treasure chest!"]
		return(success)
	elif "look" in self:
		description = ["Inside this room is a rather obsenely large weasel.", "He is guarding a old-style chest filled with what you assume is fabulous treasure."]
		return(description)
	elif "quit" in self or "exit" in self:
		return[]
	else:
		dont_understand = ["I'm sorry, I don't understand that."]
		return(dont_understand)
